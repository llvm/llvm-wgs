RFC: [https\://discourse.llvm.org/t/rfc-hexfloat-floating-point-support/75833/17](https://discourse.llvm.org/t/rfc-hexfloat-floating-point-support/75833/17)  
LLVM Code of Conduct: [https\://llvm.org/docs/CodeOfConduct.html](https://llvm.org/docs/CodeOfConduct.html)  
Date: Oct 2, 2026

Attendees:

* Aaron Ballman (chair)  
* Ariel Burton  
* Joshua Cranmer  
* Hubert Tong  
* Shafik Yaghmour  
* Rajan Bhakta  
* Sean Perry  
* Kai Nackle  
* Ian Li

Minutes:

* Aaron: constexpr support for math library functions seems to be an issue and whether llvm-libc support is needed  
* Joshua: I think it also goes into optimization, constant folding, etc. How much support do we expect to have for things like exp having an accurate implementation that the compiler knows about even on non-hexfloat systems?  
* Ariel: that would be implemented off APFloat, right?  
* Joshua: yes, but APFloat delegates the implementation to llvm-libc (at least, that’s the plan these days)  
* Ariel: with IEEE, does that get converted to a host format? Or do you use APFloat abstractions?  
* Joshua: I wish Tue was here, it’s not clear what the plans are for long double (current work focuses on float and double)  
* Rajan: Tue mentioned that he’s looking at using double double for long double, so stepping out of IEEE  
* Ariel: what are the functions we’re talking about?  
* Joshua/Aaron: C++23 adding constexpr to basically everything in math.h  
* Joshua: for HexFloat, you have to have accurate exception conditions so that it ensures it won’t be valid in constexpr if the exception is raised  
* Rajan: for non-IEEE, can we make nothing constexpr?  
* Joshua: [https\://eel.is/c++draft/library.c\#3](https://eel.is/c++draft/library.c#3)  
* Hubert: what that means is Annex F mainly tells you about inputs that are signed zeros, infinities, nans, etc. This particular sentence about Annex F are not really talking about finite inputs where you get a range error, this is more about the cases where you already have infinities involved.  
* Rajan: does the general statement from Joshua apply regarding IEEE?  
* Hubert: the standard doesn’t really say that. Elementary arithmetic cases follow the idea that overflow occurring is UB if you cannot represent it as infinity. HexFloat is fine there. As for cmath functions, there are range errors and they’re presented as exceptions in IEEE, so you map the errors and exceptions. The error is a property that holds regardless of the exceptions that you happen to raise (or rounding mode, etc). If you end up with a range or domain error, you don’t need to fold it because the constant expression will fail.  
* Sean: by fail, just won’t be constexpr?  
* Hubert: yup, if it was required to be constexpr, it’s an error, otherwise runtime evaluation  
* Sean: how much is it expected that we do support constexpr support for HexFloat? Can we do basic arithmetic, but none of the function calls will be constexpr?  
* Hubert: I don’t believe that’s conforming. The C++ committee has said that “costly” is not a reason to oppose a proposal, only “impossible”. So HexFloat needs to do the evaluation for the cmath calls. But there’s no requirement that it has to come back the same as what comes back at runtime.  
* Aaron: there is a requirement in C and there is a recommended practice in C++.  
* Shafik: I would be surprised if C++ required identical results  
* Joshua: Annex F requires things there too for runtime vs compile time; claiming compliance to Annex F does require exact equivalence  
* Hubert: yeah, it does give additional requirements  
* Aaron: user experience is part of what drives the desire to have the same results at compile time and runtime. It’s an implementation burden, but one we’ve already been requiring for llvm-libc hand-in-hand work.  
* Hubert: a difference by 1 ULP is pretty reasonable as a practical compromise, particularly because there are multiple math libraries. Some of the wording around Annex F is that there’s still a requirement even for non-IEEE types to conform to those semantics even if you don’t claim full conformance  
* Sean: somewhere in the RFC we say that we will support constexpr, but is it okay for it to not come in right away? e.g., implement in stages  
* Hubert: what are your own requirements? Once these are there, they’ll get used by the machinery to do constant folding, so you’ll change their results out from under them  
* Sean: from a product point of view, most of the people using hex float are going to be C89 users, they’re not going to be using it for newer stuff.  
* Hubert: my understanding is that some of these functions exist in C89 and there may be runtime calls in user programs where this machinery will automatically kick-in. So recompiling means they’ll get whatever QoI is there, regardless of language mode. Suppressing this folding solely for HexFloat will require updating the library all over the place to do it.  
* Joshua: there are optimizations (in the optimizer not the frontend) which will see a call to exp with a constant operand and do it at compile time in the optimizer  
* Hubert: llvm-libc has a plan for an integer-based implementation for all of the functions and that’s what they’re going to use for directed rounding modes at compile time.  
* Joshua: the machinery is not implemented yet, but they’ve got plans for how to fix stuff for non-standard floating point types. Also, I’m fine with this not being solved in v1 of the implementation, but we do need some idea of what the solution will be.  
* Rajan: I think we can get good confidence amongst ourselves that we can do this for HexFloat as well because most of that machinery isn’t depending on IEEE format.  
* Hubert: in the direction they’re moving, yes. For the initial release, I think we should limit the folding in all contexts until the machinery exists where we can do it right. We should not convert through IEEE and back again because we’re not sure that’s going to be correct  
* Sean, Aaron: I agree  
* Moving on to unnormalized values and constexpr  
* Hubert: we have no requirement that the leading hexbit be nonzero. Those values where it’s not nonzero are valid because the platform does allow operations on those values, but the C and C++ compiler never uses those operations and would not produce them out of arithmetic. The only way to get them are things like bit\_cast or type punning. C and C++ are not the only languages though and there’s inline assembly, so what to do with those values? At runtime, it’s fine, the hardware knows. At compile time, a lot of cases just work because the base algorithm deals with it. But what do we do?  
* Ariel: all the functionality is hung off APFloat. If that’s intended to mimic what the hardware does, we need to be clear whether we’re modeling after hardware normalized add or unnormalized add?  
* Hubert: what’s the difference between the two?  
* Ariel: with normalized add, you cannot get an unnormalized result even if the inputs are unnormalized. Unnormalized add can theoretically give an unnormalized result.  
* Hubert: I’m fine with normalized add, but I’m asking about the inputs. Can you have unnormalized inputs? It seems to work from testing  
* Ariel: it will be processed by normalizing operations  
* Rajan: in general, if we make a statement that any unnormalized inputs will be normalized, I think we don’t have any concerns with the constexpr side because everything will be handled as-if at runtime.  
* Ariel: Hubert’s concern raises a different issue for me; IR for C and C++ may not be useful for other languages  
* Joshua: x \+ 0 \+ 0 would go from a normalized number to an unnormalized number as part of the optimizations, if you had a requirement that the results are always normalized after a floating point operation  
* Hubert: so we’re just matching, not doing the actual operation, and if one of the operands is zero, we stop doing the operation because of that. If a user passed in a value and you’re doing return x \+ 0, what we intended to do in codegen will produce a normalized value because of the \+0. If if we match on the operands to see if one was zero to short-circuit, it would change.  
* Sean: any constant the compiler generates should be normalized; if you optimize the \+0, then if x is unnormalized?  
* Ariel: I think Joshua’s concern is that it can flow through to subsequent operations.  
* Hubert: the subsequent operation might be in assembly  
* Ariel: it’s more subtle, you could have an unnormalized value to which you add 0\. If you do that at runtime, you get a normalized value back.  
* Hubert: if you add zero to a nonzero value, the value that you get back is a representation of the same value  
* Ariel: is that guaranteed by hardware?  
* Hubert/Rajan: yes  
* Hubert: if we try to say it’s the normalizing one, then a lot of optimizations are not necessarily valid  
* Joshua: I think the existing nan propagation rules are a good model to follow. No guarantee that the result of an operation is normalized, with a footnote explaining why that might be the case  
* Hubert: it sounds like we have an action item to update the LLVM IR definition for what happens on certain operations with these types  
* Joshua: hexfloat would be the first time this would matter, but it will matter for DFP as well  
* Joshua and Ariel will work together on coming up with wording for that  
* Hubert: when Rajan mentioned that normalization happens kind of early, do we agree with how early? Just before the arithmetic? Because the result of bit\_cast is still an unnormalized representation. For C++, that separate identity matters for template arguments.  
* Rajan: I thought template arguments are based on types?  
* Hubert: for template arguments, there are objects that back them (at least in some cases) and in floating point cases they are not pure values. The C++ committee is struggling to wrap their head around nan payloads. Non-type template arguments – same value may have different representations, if there’s a different identity for that you may end up with different specializations. Because we know unnormalized hexfloat values can behave differently from normalized ones, they have a separate identity.  
* Rajan: as soon as you do an operation they’re normalized, so under what context would they behave differently?  
* Hubert: if you were to pass it to assembly and use unnormalized operations, you can use the value.  
* Ariel: so this affects DFP as well?  
* Hubert: yes, that’s why C++ went with “identical” (having the same identity) instead of “equal”.  
* Joshua: for DFP, if you have two numbers that represent the same value but different quantum exponents, are they identical for C++ template rules?  
* Hubert: it’s unclear on purpose; C++ gives us both choices  
* Rajan: so nanpayloads that are different? Are those identical or different?  
* Hubert: my understanding is that the intent is for them to be different  
* Shafik: that’s my understanding as well  
* Rajan: that somewhat implies that different quantum exponents have different identities and same for hexfloat  
* Joshua: does anyone see a reason to make a different choice for DFP quantum exponents vs unnormalized hexfloat?  
* Rajan: I don’t see a use case for hexfloat unnormalized values, but for DFP the quantum exponent matters in real cases. If someone comes up with good use cases for hexfloat, maybe that’d change my opinion, but I do see a difference.  
* Ariel: how prevalent are unnormalized hexfloat values?  
* Rajan: I’ve never seen one.  
* Hubert: if it doesn’t matter much, avoiding normalization doesn’t hurt – if nobody generates an unnormalized value, it doesn’t matter. So maybe no need to normalize the values.  
* Rajan: agreed, but that argument also applies to \+ \- 0 too  
* Joshua: I’ve seen people use \*1 to try to canonicalize the number, but I think it’s better to canonicalize explicitly  
* Ariel: where do those values come from?  
* Joshua: if you’re writing a library and want to be defensive  
* Hubert: it seems everyone is on the same page that these values would somehow be an APFloat and so it’s just the case whether the operations will normalize before operating in APFloat space. We’re not promising that the normalization will happen if you do it at runtime but we generally expect it to happen.  
* Ariel: it might be more subtle than that; sometimes it normalizes the result and not the input, and that can end up as zero if the result is unnormalized  
* Moved on to 128-bit hexfloat and whether the unused bits are padding or not.  
* Hubert: the clear answer to me is that they’re padding bits in terms of the language  
* Rajan: the user cannot count on them being a certain value  
* Ariel: correct that they don’t contribute to the value. But the POP says what happens to them  
* Rajan: that’s fine, users should not count on that behavior. We don’t need to guarantee it.  
* Ariel: does this come back to the issue with template specializations?  
* Hubert: it does, and we ignore them for template specializations and for round-tripping it’s not required to round trip  
* Ariel: we need to distinguish between APFloat that evaluate to the same value but have a different representation?  
* Hubert: yes, and the current implementation already handles that I believe.  
* Ariel: with the 128-bit format, we don’t aim to round-trip bit\_cast values.  
* Aaron: if they’re padding bits, do we run into packing issues?  
* Hubert: no  
* Joshua: we may need some changes to APFloat around the padding bits  
* Aaron: Ariel, can you summarize decisions we reached and add them to the RFC? Then we can make sure everyone is in agreement from there and likely get the RFC into accepted status.
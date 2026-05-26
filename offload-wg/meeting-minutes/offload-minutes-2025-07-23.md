# Wednesday, July 23 2025, 9:00 - 10:00 am CDT

# Agenda

  114. PR Review LIST
  115. Liboffload API


  1. Should liboffload have a "olLinkProgram" interface? ( [https://github.com/llvm/llvm-project/pull/148648](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/148648&sa=D&source=editors&ust=1779820786905911&usg=AOvVaw0K9zV2fWF6kUXGijdMs2Qy) )


  1. This could get really complicated to support interfaces to all possible compilers.
  2. Wait until liboffload matures until deciding what to do with this.  The PR will be closed for now and revisited later.  It may eventually become a separate library.


  2. "OutEvent" vs olCreateEvent ( [https://github.com/llvm/llvm-project/pull/150217](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/150217&sa=D&source=editors&ust=1779820786906730&usg=AOvVaw3p8dNPmOi-PXOXju7SAc3J) )


  1. If we do use OutEvent, do we want the event to have a field for the entry point that created it (like ur_command_t in UR)?


  1. Fix the name/description


  116. Auto-generated documentation for liboffload: [https://github.com/llvm/llvm-project/pull/147323](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/147323&sa=D&source=editors&ust=1779820786907401&usg=AOvVaw0Ik556K6zDizSLNbPDe1se) (merged)


  1. Can we get the documentation hosted somewhere? Equivalent to [openmp.llvm.org](https://www.google.com/url?q=http://openmp.llvm.org&sa=D&source=editors&ust=1779820786907718&usg=AOvVaw3T-OZamZ3bQdRF7reBsuCw)?


  1. Email Tanya Lattner


  117. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786908086&usg=AOvVaw051hjU8n6RczYG6ujPFuV1) 


  1. Intern at LLNL implementing basic interface, expect PRs in the next week or so.


  118. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786908602&usg=AOvVaw2rrjCoEmObeGfGZANlNvsl) (merged)


  1. delete


  119. GPU ASAN (alternative) prototype ready


  1. Testing out "new-new" design to avoid memory allocations/accesses altogether
  2. Are there any PRs available for review?
  3. Is there a design discussion on discourse?


  120. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786909527&usg=AOvVaw2v37hfeFv6CxkPyarIRz3k)
  2. Is this ready for review?  Are there public discussions on this?


  121. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786910003&usg=AOvVaw1CHghx9rcHwhThe_76fRDb)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786910295&usg=AOvVaw2qr6s3RxUW9Dzo1_mKGWMw)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786910568&usg=AOvVaw3075k80feCnIaUvWIVVGCM)


  122. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786910910&usg=AOvVaw357GSSTc9vwpSG3TfeTPHm)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786911158&usg=AOvVaw2YGZ-1aiBU2VVLlUxDAImH)

* * *

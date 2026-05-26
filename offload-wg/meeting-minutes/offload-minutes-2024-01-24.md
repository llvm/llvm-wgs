# Wednesday, Jan 24, 2024, 7:00 - 8:00 am PST

# Agenda (35 people)

  1. # Welcome

  2. Ics file is broken. Johannes will try again.
  3. Offload folder PR: [https://github.com/llvm/llvm-project/pull/77154](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/77154&sa=D&source=editors&ust=1779820787029401&usg=AOvVaw2jBAnkgBVLrk9MTjnpn2OY) 
  4. Possible API discussions


  1. [https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d](https://www.google.com/url?q=https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d&sa=D&source=editors&ust=1779820787030065&usg=AOvVaw1gTqNz6vBPlgVcY9n_BarK)
  2. Discussion started, see issue: [https://github.com/llvm/llvm-project/issues/79304](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/79304&sa=D&source=editors&ust=1779820787030544&usg=AOvVaw2grbhrR4ErOtpjuisVi3Oc) 


  1. Stability guarantee?
  2. Error handling
  3. Nameing, prefix, suffix
  4. Source locations
  5. Count API invocations
  6. Coding style: 


  1. Clang format everything
  2. C++, rules of LLVM
  3. API is C?


  7. "Language" libraries on top of  plugin API:


  1. Libllvmomptarget.so, Libllvmkernel.so, Libllvmjulia.so, …


  8. Unit testing, coverage testing


  5. Next steps:


  1. Do we need a separate offload pr subscribe team, something like [https://github.com/orgs/llvm/teams/pr-subscribers-offload](https://www.google.com/url?q=https://github.com/orgs/llvm/teams/pr-subscribers-offload&sa=D&source=editors&ust=1779820787032991&usg=AOvVaw0kZ7Mid7XBftIwDwjpMvJU)?


  1. Shilei will take care as soon as the folders exist
  2. Labeling (libomptarget, offload)


  2. Should we use discourse RFC for key component design discussion instead of llvm issues?
  3. ZORG offload builder (as template for people), in addition to OpenMP offload builder.
  4. Backward compatibility of user exposed env variables ([https://openmp.llvm.org/design/Runtimes.html#libopenmptarget-environment-vars](https://www.google.com/url?q=https://openmp.llvm.org/design/Runtimes.html%23libopenmptarget-environment-vars&sa=D&source=editors&ust=1779820787034727&usg=AOvVaw1YwA_A-JzwpO_1pjsQ1gpx))



# 

* * *

# 

# Fri, Jan 12, 2024, 9:00 - 10:00 am PST

# Agenda (27 people)

  1. Welcome


  * Inline notes


  2. Future meetings


  * Wednesday 7am pacific, every two weeks.


  * Starting Jan 24, 24
  * Updates to the OpenMP invite will happen too, two separate invites.


  * Alternating with the OpenMP meeting


  3. Webpage, docs, etc.


  * Talk to Anton for webpage
  * Offload folder PR: [https://github.com/llvm/llvm-project/pull/77154](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/77154&sa=D&source=editors&ust=1779820787037383&usg=AOvVaw1KUeK2kVlFaWa5yoJL3V9-) 


  * Please review


  * Sphinx webpage, like Clang and OpenMP (.llvm.org)


  4. Initial PRs


  * Offload folder PR: [https://github.com/llvm/llvm-project/pull/77154](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/77154&sa=D&source=editors&ust=1779820787038309&usg=AOvVaw0IcEZHvfeyw9tLcG4dSMjj) 
  * Move libomptarget PR: [https://github.com/llvm/llvm-project/pull/75125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/75125&sa=D&source=editors&ust=1779820787038786&usg=AOvVaw0NB3X7N6KzVTSH8azoeme1) 


  * Plan: move then "restore"; Johannes
  * Driver switch to pickup liboffload; Joseph


  * Offload will become the default path for OpenMP shortly after


  5. Naming


  * "offload" wins.


  6. Working groups


  * API Design


  * Error model, source information, …


  * Testing


  * Buildbots, unit tests, lit tests


  7. Rust compiler, offload linking


  * Will this make it easier for the rust compiler
  * Should we include/serve (NVIDIA, AMD, …) libdevice?


  * Will talk to Artem


  8.

# Wednesday, August 6 2025, 9:00 - 10:00 am CDT

# Agenda

  108. PR Review LIST


  1. Kevin to review: [https://github.com/llvm/llvm-project/pull/143491](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/143491&sa=D&source=editors&ust=1779820786898994&usg=AOvVaw0OBJR8rwjEgytWP8JgtKmt) 
  2. ATTACH [https://github.com/llvm/llvm-project/pull/149036](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/149036&sa=D&source=editors&ust=1779820786899303&usg=AOvVaw3BZpvd_rCS_ASneF9qp-fm) 


  1. Issue with dependency between data transfer and ATTACH
  2. Joseph to review again


  109. Liboffload API


  1. How can we implement out of order queues?


  1. Codeplay looking at this internally, not sure how to implement this
  2. Any work in the queue can happen in any order
  3. Currently: pool of queues, rotated in round-robin fashion


  1. Non-blocking queue destruction would make it easier to implement (i.e. making queue easy to create/destroy)
  2. Nobody objects to this.


  2. Implementing host callbacks


  1. Is having a "worker thread" that listens for signal changes on amd acceptable?
  2. Is "no calling liboffload or libcuda functions in a callback" an acceptable limitation?
  3. Enqueuing work on host from device: have a worker thread that waits for signal about kernel completing, then executing post-work code.
  4. Joseph will take a look at PRs


  3. Should olDestroyQueue block until the queue has completed? ( [https://github.com/llvm/llvm-project/pull/152132](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/152132&sa=D&source=editors&ust=1779820786901672&usg=AOvVaw1WtJDzh-6ibUAPMkpC45xy) )


  1. In OpenCL destroy queue blocks
  2. In non-blocking case, no more items can be added to the queue, but existing workloads continue to completion.


  1. Decision: non-blocking


  110. Auto-generated documentation for liboffload: [https://github.com/llvm/llvm-project/pull/147323](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/147323&sa=D&source=editors&ust=1779820786902404&usg=AOvVaw1Oz1vQxswGMYVokU4lOgpF) (merged)


  1. Can we get the documentation hosted somewhere? Equivalent to [openmp.llvm.org](https://www.google.com/url?q=http://openmp.llvm.org&sa=D&source=editors&ust=1779820786902743&usg=AOvVaw0tRNSUgD8lUDO2uBb94gMG)?


  1. Email Tanya Lattner (Benny from CodePlay)


  111. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786903202&usg=AOvVaw0FJEQ6PRBbTpW155aZbXQz) 


  1. Intern at LLNL implementing basic interface, expect PRs in the next week or so.


  1. Jonas: still need some cleanup


  112. GPU ASAN (alternative) prototype ready


  1. Testing out "new-new" design to avoid memory allocations/accesses altogether
  2. Are there any PRs available for review?
  3. Is there a design discussion on discourse?


  1. Kevin working on this, but no update yet.


  113. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786904497&usg=AOvVaw1BujyCxNw8DwKnF2B3MMtg)
  2. Is this ready for review?  Are there public discussions on this?


  1. Kevin will ask about the progress about this.



* * *

#

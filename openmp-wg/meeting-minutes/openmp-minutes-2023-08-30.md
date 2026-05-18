### 2023, Aug 30

Agenda

New 

  * [D158774: [libc] Add GPU support for `printf` and `fprintf`](https://www.google.com/url?q=https://reviews.llvm.org/D158774&sa=D&source=editors&ust=1778600246058250&usg=AOvVaw0TieWwv-3OZBnD6AgZtVQP)


  * Should allow for a lot of AMDGPU tests to be upstreamed
  * Requires vararg support on the GPU


  * Indirect codegen patches


  * Design point of whether address of indirect function has the same or different type to the address of a function
  * [[Libomptarget] Support mapping indirect host calls to device functions](https://www.google.com/url?q=https://reviews.llvm.org/D157918&sa=D&source=editors&ust=1778600246058649&usg=AOvVaw1RDGGj8LRAbDJberUqJITQ)
  * [[OpenMP] Emit offloading entries for indirect target variables](https://www.google.com/url?q=https://reviews.llvm.org/D157738&sa=D&source=editors&ust=1778600246058775&usg=AOvVaw1EBNfpn7xjVKxOnGCUND8N)


  * omp_get_num_procs() on the device not supported anymore? ([https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c#inline-9277](https://www.google.com/url?q=https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c%23inline-9277&sa=D&source=editors&ust=1778600246058982&usg=AOvVaw2e5tj4UVu2F8YqEDhGX10E))


  * OMP Places [https://www.openmp.org/spec-html/5.1/openmpse62.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.1/openmpse62.html&sa=D&source=editors&ust=1778600246059176&usg=AOvVaw060uob5vQkHkIvVys_tiGT)
  * omp_get_place_num_procs(): [https://www.openmp.org/spec-html/5.0/openmpsu134.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.0/openmpsu134.html&sa=D&source=editors&ust=1778600246059327&usg=AOvVaw1G8iUkJhNwsuRDh7Ggf3pP)



### 

### 023, Aug 23

Agenda

New 

  * Indirect codegen patches


  * Design point of whether address of indirect function has the same or different type to the address of a function
  * [[Libomptarget] Support mapping indirect host calls to device functions](https://www.google.com/url?q=https://reviews.llvm.org/D157918&sa=D&source=editors&ust=1778600246059792&usg=AOvVaw2Em6uFwHMr-ORjwLui67Za)
  * [[OpenMP] Emit offloading entries for indirect target variables](https://www.google.com/url?q=https://reviews.llvm.org/D157738&sa=D&source=editors&ust=1778600246059910&usg=AOvVaw1b17CZeVFGfgn4sL3UJSQd)


  * Get a policy decision if we should generate errors in compiler or runtime for unsupported OpenMP APIs


  * Should get a link time error.


  * Unsuccessful conversion from generic to generic SPMD
  * omp_get_num_procs() on the device not supported anymore? ([https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c#inline-9277](https://www.google.com/url?q=https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c%23inline-9277&sa=D&source=editors&ust=1778600246060370&usg=AOvVaw1WqpoQnGdYUEy7Xd3usRMm))


  * OMP Places [https://www.openmp.org/spec-html/5.1/openmpse62.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.1/openmpse62.html&sa=D&source=editors&ust=1778600246060514&usg=AOvVaw392Ia0_x5t45sdhWdAW5l_)
  * omp_get_place_num_procs(): [https://www.openmp.org/spec-html/5.0/openmpsu134.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.0/openmpsu134.html&sa=D&source=editors&ust=1778600246060657&usg=AOvVaw1RG5XV-fIsm3L9u80KQXfv)


  * Update our clang support page


  * [https://clang.llvm.org/docs/OpenMPSupport.html](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html&sa=D&source=editors&ust=1778600246060821&usg=AOvVaw17C6a1_ozxZRgnlIBH4xBr)


  * OMPT: Missing callbacks in plugin generic-elf-64bit: [https://github.com/llvm/llvm-project/issues/64487](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/64487&sa=D&source=editors&ust=1778600246060989&usg=AOvVaw0HLlB9O2tzjULASIfINAUF)


  * How to proceed with the plugin? [https://reviews.llvm.org/D158542](https://www.google.com/url?q=https://reviews.llvm.org/D158542&sa=D&source=editors&ust=1778600246061454&usg=AOvVaw0mJdzd6OmUIy2n41LyHJ-f)
  * Simply connect OMPT and be done with it? [https://reviews.llvm.org/D158543](https://www.google.com/url?q=https://reviews.llvm.org/D158543&sa=D&source=editors&ust=1778600246061598&usg=AOvVaw1nd-BvCTbMVBVrXuVKfNuj)



###

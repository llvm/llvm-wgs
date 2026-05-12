### 2021, March 3rd

### Agenda

  * Interop construct
  * Requires unified_shared_memory
  * Embedding info in fat binary using elf format
  * Omp_get_num_devices


  * Without target region: returns number of devices, when compiling with -fopenmp-targets=nvptx64-nvidia-cuda
  * [https://reviews.llvm.org/D97616](https://www.google.com/url?q=https://reviews.llvm.org/D97616&sa=D&source=editors&ust=1778600246566267&usg=AOvVaw3q0fT8wlkhyXisjXyU3GN6)


  * Simplifying and optimizing GPU globalization code


  * [https://reviews.llvm.org/D97680](https://www.google.com/url?q=https://reviews.llvm.org/D97680&sa=D&source=editors&ust=1778600246566426&usg=AOvVaw2DsRRn1XS7YOWl5wDFW3GD)
  * [https://reviews.llvm.org/D97818](https://www.google.com/url?q=https://reviews.llvm.org/D97818&sa=D&source=editors&ust=1778600246566520&usg=AOvVaw0RmT5G1BLOW_fnluye9TyA)


  * Constant struct firstprivate arguments creating static constant memory in the device


  * [https://godbolt.org/z/vMaaxj](https://www.google.com/url?q=https://godbolt.org/z/vMaaxj&sa=D&source=editors&ust=1778600246566691&usg=AOvVaw0Gcc3aYMjRqpcxdW-dtGmt)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=49334](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49334&sa=D&source=editors&ust=1778600246566840&usg=AOvVaw083EOIpsNSVcZAGIp51I9g) (12 blocking)
  * [https://bugs.llvm.org/show_bug.cgi?id=49339](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D49339&sa=D&source=editors&ust=1778600246566963&usg=AOvVaw3aWgKkApJZ29Ik7AvM_uK-) (12 blocking)



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * George Rokos (Intel)
  * Joseph Huber (ORNL)
  * Ravi Narayanaswamy (Intel)
  * Andrey Churbanov (Intel)
  * Johannes Doerfert (ANL)
  * Saiyedul Islam, Ron Lieberman, Ethan Stewart, Raghu (AMD)
  * Joel Denny (ORNL)
  * Simon Garcia de Gonzalo (BSC)

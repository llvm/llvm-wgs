### 2020, December 02

### Agenda

  * libomptarget image registration order


  * Manoel will look into this further, propose a patch


  * get_num_devices/get_device_num on gpu
  * Fat archive library


  * Link only needed routines.
  * Split into 4 patches


  1. [Landed] [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246582391&usg=AOvVaw2KgDNrJCmdFyLMQPyX8R5s): llvm-link: Add support for archive files as inputs
  2. [Under review] [https://reviews.llvm.org/D80816](https://www.google.com/url?q=https://reviews.llvm.org/D80816&sa=D&source=editors&ust=1778600246582554&usg=AOvVaw3Bm7AXNrfNxWVJTnVyXqYk): [OpenMP] Add unbundling of archives containing bundled object files into device specific archives (modifications to clang-offload-bundler tool)
  3. [Yet to publish on phab] Clang's mlink-builtin-bitcode - CGCodeGenAction.cpp
  4. [Yet to publish on phab] Modify toolchain to extract archive


  * Concurrent map(to:) - accepting overlapping regions vs copying simultaneously (also D86119)
  * Embedded image versioning in Fat binary
  * 


### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * George Rokos (Intel)
  * Johannes Doerfert (ANL)
  * Ravi Narayanaswamy (Intel)
  * Joseph Huber (ORNL)
  * Raghu Maddhipatla(AMD)
  * Andrey Churbanov (Intel)
  * Saiyedul Islam (AMD)
  * Kelvin Li (IBM)
  * Jose M Monsalve Diaz (ANL/UD)\
  * Valentin Clement (ORNL)

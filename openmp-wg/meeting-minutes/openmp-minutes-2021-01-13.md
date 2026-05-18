### 2021, January 13

### Agenda

  * Status of async offloading 
  * Appending line numbers into symbol names
  * Patches in flight to drop nvcc built static library and change to openmp (D94573, D93135)
  * Steps towards building the device runtime with clang only (e.g. ENABLE_RUNTIMES)
  * Steps towards offloading capabilities in release LLVM builds (on Ubuntu, …)


  * Build runtime libraries on machine without cuda, hsa installed
  * Libm requires vendor library, but doesn't strictly 'need' vendor headers


  * CUDA/HSA/… definitions can come in late, that is during user code compilation, device runtime can stop with (wrapper) declarations


  * Single interface for parallel regions on device & host
  * TRegion init/deinit + state machine will be revived, helped by OpenMP opt state machine customization



### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert (ANL)
  * George Rokos (Intel)
  * Jon Chesterfield (AMD)
  * Joseph Huber (ORNL)
  * Roger Ferrer Ibañez (Barcelona Supercomputing Center)
  * Saiyedul Islam (AMD)
  * Andrey Churbanov (Intel)
  * Kelvin Li (IBM)
  * Raghu Maddhipatla (AMD)
  * Joel Denny (ORNL)
  * Valentin Clement (ORNL)

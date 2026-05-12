### 2023, Dec 06

Agenda 

New 

  * Question on [https://github.com/llvm/llvm-project/pull/74532](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/74532&sa=D&source=editors&ust=1778600246046747&usg=AOvVaw3vQ8UCdZgr74ZnG9HSEtAV) 
  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246046978&usg=AOvVaw09vTOSSfJFCCVORTMRVrxI)


  * Plugin unit tests: [https://github.com/llvm/llvm-project/pull/74398](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/74398&sa=D&source=editors&ust=1778600246047148&usg=AOvVaw3cmeL0sNJmR29_b956kjY3)
  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246047383&usg=AOvVaw2hq6rtQZUHtgD5Ivlt4TTe) (-DLLVM_ENABLE_PROJECTS=openmp): 34 failed tests
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246047517&usg=AOvVaw1YFoWoVT2b99Q0PipGIpn7) (-DLLVM_ENABLE_RUNTIMES=openmp): 34 failed tests
  * [[libomptarget][tests] Maximum assumed device heap size. * Issue #71747](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/71747&sa=D&source=editors&ust=1778600246047688&usg=AOvVaw1cUPV7X-Sm3vKDMZ-dBB_-) (4 tests)

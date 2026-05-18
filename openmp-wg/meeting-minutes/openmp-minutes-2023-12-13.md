### 2023, Dec 13

Agenda 

New 

  * Impact of device initialization reorganization [[OpenMP] Reorganize the initialization of `PluginAdaptorTy` by jdoerfert * Pull Request #74397 * llvm/llvm-project (github.com)](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/74397&sa=D&source=editors&ust=1778600246045505&usg=AOvVaw1iE-ayr2G_1moUVjlMwvmW)
  * Who uses a project build of libomptarget and why?
  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246045798&usg=AOvVaw2nqlXYgXMNdVMYds2jW0AB)


  * Plugin unit tests: [https://github.com/llvm/llvm-project/pull/74398](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/74398&sa=D&source=editors&ust=1778600246045929&usg=AOvVaw3kbk1jvhF1vUBHrs5_OMG7)
  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246046171&usg=AOvVaw3SngeNuzMjfgQldf6CZxTs) (-DLLVM_ENABLE_PROJECTS=openmp): 34 failed tests
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246046309&usg=AOvVaw1tpX-VNKwi2TqeqDQDmgxn) (-DLLVM_ENABLE_RUNTIMES=openmp): 34 failed tests
  * [[libomptarget][tests] Maximum assumed device heap size. * Issue #71747](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/71747&sa=D&source=editors&ust=1778600246046479&usg=AOvVaw36V3SBODgBOkKcKioQTUUP) (4 tests)

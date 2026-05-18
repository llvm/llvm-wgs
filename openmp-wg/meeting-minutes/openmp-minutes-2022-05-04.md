### 2022, May 4

Agenda

  * Compiling CUDA with the new driver is up for review [https://reviews.llvm.org/D123812](https://www.google.com/url?q=https://reviews.llvm.org/D123812&sa=D&source=editors&ust=1778600246318637&usg=AOvVaw3QMEue02hejQJryBsFmLEg). Allows OpenMP Offloading to be compiled with and call CUDA.
  * Patch that allows OpenMP to use -offload-arch= [https://reviews.llvm.org/D124721](https://www.google.com/url?q=https://reviews.llvm.org/D124721&sa=D&source=editors&ust=1778600246318830&usg=AOvVaw2oaxgT1q7j5oQLFGJjYuTK)


  * Should we infer -fopenmp-target= if --offload-arch is present?
  * Can be used to make static libraries supporting multiple architectures as needed.


  * Should we embed the -cuda-install path into the device binary at compile time and use that?


  * Every PTX file is expected to be made with a valid CUDA install
  * It's possible that the install could've changed between compilation and building


  * Could default to $PATH if not found


  * Multi-arch compilation support


  * First patch in the series posted for review:


  * [D124525](https://www.google.com/url?q=https://reviews.llvm.org/D124525&sa=D&source=editors&ust=1778600246319569&usg=AOvVaw1i0Qr-vvOOSOQ8X36ojFw0): [OpenMP][ClangLinkerWrapper] Extending linker wrapper to embed metadata for multi-arch fat binaries


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory
  * Lambda captures
  * "Post processing" for lookups w/o reference count updates

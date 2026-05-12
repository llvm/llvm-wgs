### 2023, july 19

Agenda

New 

  * Update our clang support page


  * https://clang.llvm.org/docs/OpenMPSupport.html


  * Target annotations for tuning (min/max workgroup size, etc.)



#pragma omp target teams distribute parallel for ompx_attribute(amdgpu_waves_per_eu(6), amdgpu_flat_work_group_size(64, 256), __launch_bounds__(256, 6))  num_teams(NumTeams) thead_limit(ThreadLimit)

                                         for (...)

  * Kevin is picking up reductions
  * OpenMC and Kokkos have new problems (need to debug before release, after branch)
  * Next time: Testing libm-gpu.a,  WIP, Anton will talk about it soon: 


  * [timing_histograms (1).pdf](https://www.google.com/url?q=https://drive.google.com/file/d/1ZK9J-iJAFjb7cQb7ghP6xSqMbUukeRXW/view?usp%3Dshare_link&sa=D&source=editors&ust=1778600246066352&usg=AOvVaw2JpiIWJAPGa2a835J4mqfr)
  * [error_plots (1).pdf](https://www.google.com/url?q=https://drive.google.com/file/d/1372FZKRRPTuERCAuJrAls7Q5zI4LsRfj/view?usp%3Dshare_link&sa=D&source=editors&ust=1778600246066461&usg=AOvVaw3lI9ilnVrIERFI9oNnOBmL)

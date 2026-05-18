### 2021, June 9th

### Agenda

  * Talk tomorrow: [https://www.openmp.org/events/webinar-a-compilers-view-of-the-openmp-api/](https://www.google.com/url?q=https://www.openmp.org/events/webinar-a-compilers-view-of-the-openmp-api/&sa=D&source=editors&ust=1778600246547388&usg=AOvVaw37wGhydaz0vAlPpgWziH-p)
  * Proceed with the ELF notes changes based on LLVM ELF
  * Offloading buildbot https://lab.llvm.org/staging/#/workers/118 (Michael)


  * For bug49334.cpp (http://llvm.org/PR49334) to make it failing steadily, reduce the size of the matrix (BS = 16; /  N = 256;)


  * https://lab.llvm.org/staging/#/builders/155/builds/444
  * https://lab.llvm.org/staging/#/builders/154/builds/175 (bug49334.cpp)


  * https://lab.llvm.org/staging/#/builders/155/builds/263 (api/omp_get_wtime)
  * https://lab.llvm.org/staging/#/builders/154/builds/194, https://lab.llvm.org/staging/#/builders/154/builds/301 (depend.cpp)
  * https://lab.llvm.org/staging/#/builders/155/builds/444 (gtid.cpp)


  * Llvm-link archive support? [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246548251&usg=AOvVaw17cAewK9WZqHVjRalcjDv8) ? [https://reviews.llvm.org/D93525](https://www.google.com/url?q=https://reviews.llvm.org/D93525&sa=D&source=editors&ust=1778600246548335&usg=AOvVaw0KZZm9FX7AOv5Pwji6BDBk)
  * Finding static libraries with "-lstaticlib" option
  * Scheduling OMPT topics
  * Write a CMake module for OpenMP Offloading?



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=50642](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50642&sa=D&source=editors&ust=1778600246548669&usg=AOvVaw1A4oI0nHOvaZ5Z82jxehf5)
  * [https://bugs.llvm.org/show_bug.cgi?id=50640](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50640&sa=D&source=editors&ust=1778600246548799&usg=AOvVaw2mkmTHsGgH7htmw1uvWytH)
  * https://bugs.llvm.org/show_bug.cgi?id=50619



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert (ANL)0
  * Carlo Bertolli (AMD)
  * Jon Chesterfield (AMD)
  * John Mellor-Crummey (Rice)
  * Andrey Churbanov (Intel)
  * Vladimir Indjic (University of Novi Sad)
  * Joseph Huber (ORNL)
  * Saiyedul Islam (AMD)
  * George Rokos (Intel)
  * Joel Denny (ORNL)

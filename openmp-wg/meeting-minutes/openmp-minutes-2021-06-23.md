### 2021, June 23rd

### Agenda

  * New globalization got merged  :)
  * Elf cleanup in libomptarget 
  * Async offload status
  *   Offloading buildbot https://lab.llvm.org/staging/#/workers/118 (Michael)


  * https://llvm.org/PR50739 (Race condition in bug49334.cpp)


  * [https://reviews.llvm.org/D104382](https://www.google.com/url?q=https://reviews.llvm.org/D104382&sa=D&source=editors&ust=1778600246543393&usg=AOvVaw0hVI76BGERixBm-RCWJ5YW)
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246543500&usg=AOvVaw3RkcpiUe9GQrxaA1BN-c2y)
  * [https://reviews.llvm.org/D104555](https://www.google.com/url?q=https://reviews.llvm.org/D104555&sa=D&source=editors&ust=1778600246543590&usg=AOvVaw3QvKTpsQPz3zU42J6TrDIy) (potentially can also fix for host offloading)


  * Device specific archive library


  * Llvm-link archive support? [https://reviews.llvm.org/D81109](https://www.google.com/url?q=https://reviews.llvm.org/D81109&sa=D&source=editors&ust=1778600246543789&usg=AOvVaw0lsRon04j34C9DNpuETpNJ) (merged)
  * Unbundling of device specific archive from fat archive [https://reviews.llvm.org/D93525](https://www.google.com/url?q=https://reviews.llvm.org/D93525&sa=D&source=editors&ust=1778600246543941&usg=AOvVaw01SJdIarI-STaiuSR_5IL8) (under review)


  * Implementation of serialized parallel regions in OpenMP vs. OMPT
  * CMake find module for offloading [https://reviews.llvm.org/D104710](https://www.google.com/url?q=https://reviews.llvm.org/D104710&sa=D&source=editors&ust=1778600246544163&usg=AOvVaw0Ply5cLKUaw2GskQMwzFRV)



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=50640](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50640&sa=D&source=editors&ust=1778600246544317&usg=AOvVaw0Kyka5IMP7srjL6L1PpTmb)
  * [https://bugs.llvm.org/show_bug.cgi?id=50619](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D50619&sa=D&source=editors&ust=1778600246544423&usg=AOvVaw266uuIH77_o2dg2RGIapUQ)



### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Vladimir Indjic (University of Novi Sad)
  * Joseph Huber (ORNL)
  * Jon Chesterfield (AMD)
  * Johannes Doerfert (ANL)
  * Andrey Churbanov (Intel)
  * Raghu Maddhipatla(AMD)
  * Saiyedul Islam (AMD)
  * Joel Denny (ORNL)

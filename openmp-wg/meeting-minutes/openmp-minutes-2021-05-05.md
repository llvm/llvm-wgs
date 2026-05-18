### 2021, May 5th

### Agenda

  * Interop object extension with implementation-defined info
  * Helper thread degradation.
  * [https://reviews.llvm.org/D101173](https://www.google.com/url?q=https://reviews.llvm.org/D101173&sa=D&source=editors&ust=1778600246553676&usg=AOvVaw0a5oh6fm54ZkARBgNPqD0x)
  * Virtual functions: vtable is generated for a constructor definition, and its initializer references all virtual functions that are declared within the class; does it mean that all virtual functions' definitions must be marked "declare target"?  Otherwise, if a device side vtable is ever created, some references may be unresolved.
  * (Greg) Enhanced multi-image support .  Requirements/Capabilities model 



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=48851](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D48851&sa=D&source=editors&ust=1778600246554238&usg=AOvVaw1PCitvk_6fTwoH-TbTFfJ_) (refresher)



### Patches to look at

  * OMPD: [https://reviews.llvm.org/D100181](https://www.google.com/url?q=https://reviews.llvm.org/D100181&sa=D&source=editors&ust=1778600246554409&usg=AOvVaw0w3QXqltomouhffD_eQ11N) and followups



### Participants (voluntary/incomplete listing)

  * Johannes Doerfert, Ye Luo (ANL)
  * Ravi Narayanaswamy (Intel)
  * Jon Chesterfield (AMD)
  * George Rokos (Intel)
  * Natalia Glagoleva (Microsoft)
  * Chris Pulido (Microsoft)
  * Andrey Churbanov (Intel)
  * Carlo Bertolli (AMD)
  * Joel Denny (ORNL)
  * Saiyedul Islam (AMD)

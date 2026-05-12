### 2021, May 12th

### Agenda

  * (Greg) Enhanced multi-image support .  Requirements/Capabilities model 
  * Interop object extension with implementation-defined info


  * Deepak to bring it up in OpenMP Accel Committee


  * Helper thread degradation.
  * Static device archives with device code: https://reviews.llvm.org/D93525
  * Virtual functions: vtable is generated for a constructor definition, and its initializer references all virtual functions that are declared within the class; does it mean that all virtual functions' definitions must be marked "declare target"?  Otherwise, if a device side vtable is ever created, some references may be unresolved.
  * 


### Open Bugs

  * 


### Patches to look at

  * OMPD: [https://reviews.llvm.org/D100181](https://www.google.com/url?q=https://reviews.llvm.org/D100181&sa=D&source=editors&ust=1778600246552938&usg=AOvVaw1u8IUNeeufA7DwHtyEhqve) and followups
  * Custom state machine & SPMD detection [https://reviews.llvm.org/D101977](https://www.google.com/url?q=https://reviews.llvm.org/D101977&sa=D&source=editors&ust=1778600246553085&usg=AOvVaw11kYEpcKL5rrgQNeoftN6n) and stack



### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * George Rokos (Intel)
  * Jon Chesterfield (AMD)
  * Johannes Doerfert (ANL)
  * Saiyedul Islam (AMD)

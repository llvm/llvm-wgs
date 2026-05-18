### 2020, October 7

### Agenda

  * Setenv use in the runtime: [http://lists.llvm.org/pipermail/openmp-dev/2020-September/003652.html](https://www.google.com/url?q=http://lists.llvm.org/pipermail/openmp-dev/2020-September/003652.html&sa=D&source=editors&ust=1778600246592830&usg=AOvVaw2oorDGksOsPhuBbOmDkxB3)


  * Intel has an implementation that work.  There are some corner case Todd is working.


  * Plans for detached task?


  * Intel has a version implemented according to OpenMP Spec in the runtime
  * Frontend has some use of detached task..


  * b09cce07c7ebd6d42c97f7144f5a2e7dd8fca19e


  * Walk through the list and keep it up to date: [https://clang.llvm.org/docs/OpenMPSupport.html#basic-support-for-cuda-devices](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23basic-support-for-cuda-devices&sa=D&source=editors&ust=1778600246593381&usg=AOvVaw1GbJQFuBTjPj8XA3VyxnyW)


  * There are some line items marked unclaimed.  This may be due to the reason the description is not clear on what needs to be done.


  * Discuss location pointers in target runtime functions and augmenting the mapper functions with variable declaration names. [https://reviews.llvm.org/D87946](https://www.google.com/url?q=https://reviews.llvm.org/D87946&sa=D&source=editors&ust=1778600246593715&usg=AOvVaw1X2fqAVElWruya_xYRGrmX)


  * Adding ident  support need to add new API.
  * Add array of struct with name, line and column


  * Map types PTR_AND_OBJ  reused for PTR (named array)


  * George will send an example to clarify the issue.


  * Fat archive libraries.
  * Conflicting host and target pointer width errors.[ https://reviews.llvm.org/D88594 ](https://www.google.com/url?q=https://reviews.llvm.org/D88594&sa=D&source=editors&ust=1778600246594137&usg=AOvVaw1AUfnhG26cTV4Mhq-tWmOb)
  * [http://openmp.llvm.org/docs](https://www.google.com/url?q=http://openmp.llvm.org/docs&sa=D&source=editors&ust=1778600246594232&usg=AOvVaw261guA2Qi6QF8tVFnBciJY)
  * GPU variable globalization work (quick update)
  * 


### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert, Ye Luo (ANL)
  * George Rokos (Intel)
  * Andrey Churbanov (Intel)
  * Joseph Huber (ORNL)
  * Jose M Monsalve Diaz (ANL/UD)
  * Valentin Clement (ORNL)
  * Joel Denny (ORNL)



###   
2020, September 16

### Agenda

  * IWOMP and OpenMP F2F next 2 weeks.  


  * Next 2 weeks cancelled.


  * Clang OpenMP tests rewrite using update_cc_test_checks.py


  * Looking to supporting global variables
  * Teach script about run lines and how to test them.
  * Then start updating FE tests to use scripts
  * [Islam] Is the plan for new tests or current tests


  * [Johannes] Also for current tests
  * [https://reviews.llvm.org/D83004](https://www.google.com/url?q=https://reviews.llvm.org/D83004&sa=D&source=editors&ust=1778600246595539&usg=AOvVaw1reJnMxM5fI6lJif95aoka)
  * [https://reviews.llvm.org/D85932](https://www.google.com/url?q=https://reviews.llvm.org/D85932&sa=D&source=editors&ust=1778600246595666&usg=AOvVaw2IXLYUH_OG3oLgBbh1SRsG) 


  * Print variable names in  mapped clause in libomptarget


  * Extend the API
  * Have a new function called in debugging mode to map address to names


  * FE uses 0 size for is_device_ptr pointers and non-zero size for firstprivate literals,


  * FE may already be doing this.
  * Add a new map type which is a clean solution.


  * Moderator for the OpenMPOpt tech talk @LLVM-Dev:


  * [https://whova.com/embedded/session/llvm_202010/1162344/?view=](https://www.google.com/url?q=https://whova.com/embedded/session/llvm_202010/1162344/?view%3D&sa=D&source=editors&ust=1778600246596279&usg=AOvVaw3UcDA6Vka0IJUxKqJpeKCH)



Usually I request volunteers from the community to moderate the talks at the dev meeting. However, given that we are in a virtual format, moderators will have a much larger role.  

 

Moderators will be asked to moderate the live Q&A portion of your talk. They will take questions from the audience through the Whova Q&A feature. They also should have a couple questions prepared in the event that no questions are submitted. 

 

It would be extremely beneficial to have a moderator who is familiar with your work. This might be an author, co-worker, or someone you know in the LLVM community. 

 

I'm asking all speakers to try to recruit a moderator for your talk by September 18th. Once you have a moderator, please have them fill out this form: 

https://forms.gle/8o4kP2uQdwvnPdWF8 <https://forms.gle/8o4kP2uQdwvnPdWF8>

 

Moderators will participate in a training session that is listed on the form and they can select their day/time.

  * is _initial_device update
  * Issue with declare variant.


  * The names in declare variant is mangled but the call is not.


  * Are we still required to keep libomptarget independent from llvm? In particular there's some unfortunate duplication going on because we can't #include one file from both, I think on licensing grounds, but it looks like libomp has the same license as llvm now. Propose that we declare that the LLVM source tree is required on disk in order to build libomp, and take a CMake variable pointing to it, so we can #include various constants. That'll annoy whoever is building libomp without clang, but on balance it seems reasonable to ask whoever is doing that to download a few source files.



### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Jon Chesterfield (AMD)
  * George Rokos (Intel)
  * Saiyedul Islam (AMD)
  * Ron Lieberman (AMD)
  * Johannes Doerfert (ANL)
  * Valentin Clement (ORNL)
  * Joel Denny (ORNL)
  * Jose M Monsalve Diaz (UDEL/ANL)
  * Andrey Churbanov (Intel)
  * Shilei Tian (SBU)
  * Joseph Huber (ORNL)
  *

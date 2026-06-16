# Wednesday, September 17 2025, 9:00 - 10:00 am CDT

# Agenda

  90. PR Review list


  1. 

  91. Location for scripts / Infrastructure for testing (JP)


  1. Consolidate scripts that the buildbots run into llvm-project. Makes reproducibility better as it ties the scripts to the LLVM version. Also enables developers to easier recreate what the buildbots do locally. 
  2. We already have the container recipes  public, CMake cache files are in-tree that are used for the build. What's left is the actual scripts that are run when testing.
  3. Immediate ideas where to put these:


  1. llvm-project/offload/ci 


  4. No concerns


  92. Liboffload API


  1. Further discussion on device/memory allocation link - in regards to [https://github.com/llvm/llvm-project/pull/154733](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154733&sa=D&source=editors&ust=1779820786876157&usg=AOvVaw1sp97uNKAco6rXr_OHSkKV)  (closed), new PR: [https://github.com/llvm/llvm-project/pull/157478](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/157478&sa=D&source=editors&ust=1779820786876432&usg=AOvVaw3dqiMhlKbVKy0B6QDhdP1Q) 


  1. Binary search to find memory addresses is not possible or difficult since memory regions can overlap in weird ways for device allocations.
  2. Using a map has similar problems - we'd need to do a linear search to find the appropriate key anyway.
  3. We need AllocInfo for a hypothetical olGetMemInfo method which can query an allocations type, base and size.


  1. Sadly it doesn't seem possible to query this information directly from the pointer through HSA.
  2. We could also not provide this information and require the liboffload user to track it themselves if they need it.


  4. AllocInfo is also used to find the platform used for host/managed allocations.


  1. Wouldn't need this requirement if the "device" parameter to olMemFree was mandatory.
  2. Without olGetMemInfo and with olMemFree only allowing the start of the buffer we wouldn't need to track the size.
  3. Could we allocate an extra 8 bytes and use the start of the buffer to store the device handle?


  5. Piotr is keen on not having olMemCpy (and friends) not accept a device pointer, is this feasible?


  1. Required to identify whether the transfer is host to device, device to host or device to device.
  2. Required to identify the device itself, and which platform to use (could be queried through the queue instead?)
  3. Specifying both allows the API in the future to be able to transfer data from completely separate devices (using the host as an intermediate).


  6. Pass device id to alloc/free vs pass plugin id


  1. Joseph: it's easier for the user to keep track of the platform/plugin
  2. Runtime tracks active plugins
  3. In free, query the plugin for pointer info first


  7. Joseph: why can't we re-allocate if we got a duplicate address from allocation?  Keeping track of platforms adds too much burden on the user.


  1. Ross: We'd like to get the "owner" of each valid address.
  2. Joseph: In case of USM, the linux kernel should manage the address space.
  3. Sergey: Different drivers do not communicate with one another.
  4. Joseph: It's very unlikely to get a conflict, re-allocation would be rare
  5. Piotr: Multiple devices are common with integrated GPUs.


  8. Concern with memcpy having to do pointer lookup: may not be worth the effort.


  1. If memcpy took device ids the lookup wouldn't be needed
  2. Ross: there is a use-case with bare pointers
  3. Unified RT needs to know if the pointer is on host or on an actual device
  4. Further discussion to be continued in the PR


  2. Callum and Ross will stop working on the liboffload at the end of the month.  Intel will pick up the work.


  93. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786882146&usg=AOvVaw3Igrumhb37xWYza14mQwJY) 


  1. Jonas is implementing basic interface, expect more PRs in the next week or so.


  1. [https://github.com/llvm/llvm-project/pull/156259](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/156259&sa=D&source=editors&ust=1779820786882607&usg=AOvVaw3aek7CPT8PEcdkGo2T6XlM)


  1. Joseph added comments to the PR, waiting for response
  2. Jonas's internship has ended, but he will continue working on this (at a slower pace, perhaps).


  2. More PRs coming soon


  94. Parallel Thin LTO (WIP) 


  1. Some parts are already in upstream. Shilei (?) has been working on that
  2. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786883645&usg=AOvVaw1S5tf4tvBjfFVIHDUJGBbW)


  95. Level zero plugin


  1. Review in progress



* * *

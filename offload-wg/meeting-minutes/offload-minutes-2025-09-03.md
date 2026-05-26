# Wednesday, September 3 2025, 9:00 - 10:00 am CDT

# Agenda

  96. PR Review LIST


  1. 

  97. Location for scripts / Infrastructure for testing (JP)


  1. Consolidate scripts that the buildbots run into llvm-project. Makes reproducibility better as it ties the scripts to the LLVM version. Also enables developers to easier recreate what the buildbots do locally. 
  2. We already have the container recipes  public, CMake cache files are in-tree that are used for the build. What's left is the actual scripts that are run when testing.
  3. Immediate ideas where to put these:


  1. llvm-project/offload/ci 
  2. llvm-project/.ci/offload
  3. llvm-project/offload/infra


  98. Liboffload API


  1. Further discussion on device/memory allocation link - in regards to [https://github.com/llvm/llvm-project/pull/154733](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154733&sa=D&source=editors&ust=1779820786886050&usg=AOvVaw1NI-XkZDZh5kOiriLlljsv) 


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
  4. 

  2. [https://github.com/llvm/llvm-project/pull/155626](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/155626&sa=D&source=editors&ust=1779820786889641&usg=AOvVaw08thW458VmXL3ae4akHGiC) \- Replace openmp offload info with liboffload one? Would mean losing some vendor specific data.


  1. Perhaps improve output format, otherwise good to merge


  99. Can we get offload documentation hosted somewhere? Equivalent to [openmp.llvm.org](https://www.google.com/url?q=http://openmp.llvm.org&sa=D&source=editors&ust=1779820786890236&usg=AOvVaw3HdD2Oy3k5bcDAovQFgodc)?


  1. Email Tanya Lattner (Someone from Codeplay)


  1. Callum will follow-up, (can also email Brittany Watson [bwatson@llvm.org](mailto:bwatson@llvm.org), Tanya's backup)


  1. No response yet


  100. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786891030&usg=AOvVaw2iOsdZ8GsAhDMX7oCFXJa_) 


  1. Jonas is implementing basic interface, expect more PRs in the next week or so.


  1. [https://github.com/llvm/llvm-project/pull/156259](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/156259&sa=D&source=editors&ust=1779820786891475&usg=AOvVaw3eKZjzTu6tVwNNuX6l9Qjy)
  2. More PRs coming soon


  101. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786891904&usg=AOvVaw2Tg4fUWSQSfWa04DCdF5wF)
  2. Is this ready for review?  Are there public discussions on this?


  1. Kevin will ask about the progress about this.

* * *

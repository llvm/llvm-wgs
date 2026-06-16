# Wednesday, Feb 19  2025, 7:00 - 8:00 am PST

# Agenda

  176. PR Review LIST


  1. Implement the remaining initial Offload API: [https://github.com/llvm/llvm-project/pull/122106](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/122106&sa=D&source=editors&ust=1779820786942037&usg=AOvVaw0RsLWqC8PMWh9gpAI-OuZE)


  177. Liboffload API


  1. Second PR is ready for review (see earlier link). Enough to get a simple SYCL program working on offload.


  1. Some changes based on review feedback - reverted plugin changes and added a new version of memcpy that takes a special host device to represent copies to/from host. Old memcpy versions are still included for comparison. Is everyone happy with the new version?
  2. Follow-up PR includes testing with device binaries for program & kernel testing. WIP but available here: [https://github.com/llvm/llvm-project/pull/127803](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/127803&sa=D&source=editors&ust=1779820786943181&usg=AOvVaw3ThJm3IY95wTQmfUhGTzXQ) (only the last commit)


  178. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786943643&usg=AOvVaw1iZGSTPrH2wNA1d3louR1z)


  179. GPU ASAN (alternative) prototype ready



# Testing out "new-new" design to avoid memory allocations/accesses all together

* * *

#

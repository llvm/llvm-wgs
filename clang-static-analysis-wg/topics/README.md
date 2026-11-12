# Topics

*This is a rough sketch of the topics, and the table keeping track of our priorities and interests.*

1. Tidy and CSA checker naming scheme: let’s use labels
2. Discuss the current state of [[clang::suppress]].
   - This should work across clang tools.
   - Do we have any blockers for user adoption?
     - I know that CSA does not suppress bugs if the attribute has arguments.
3. Clang-tooling auto discovers `compile_commands.json`
   - This causes problems with vfsoverlay, [#182526](https://github.com/llvm/llvm-project/issues/182526)
   - Hard-to-debug failure mode.
   - This auto discovery breaks multi arch builds using 2 stage builds.
4. SARIF support gaps across clang tools.
5. What could we use `llvm::cas` for? (granular caching opportunities)
6. Discuss how could we use the `__counted_by` and `-fbound-safety` annotations in different clang tooling.
7. Discuss Scalable Static Analysis Framework (SSAF) and the use of the summaries from other clang-tooling.
8. Traversal of `TUDecl` deserializes the whole module.
   - This impacts CSA, clang-tidy, or anything building a ParentMapContext.
   - One potential solution would be setting the traversal scope.

## New subjects

9. Improving `CallGraph` compile-times.
10. Pre-commit CI for analyze-time regressions (and possibly even for surfacing false positives on a golden test project like LLVM itself).

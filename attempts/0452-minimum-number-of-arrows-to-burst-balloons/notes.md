# LC 452 Minimum Number of Arrows to Burst Balloons

## 2026-11-19 · A · 15min

- 一遍过。按左端排序，right 维护当前这一箭覆盖的所有气球右端最小值。
- 用 `>`：区间是闭区间，相切（左端 == right）也能被同一箭射爆。
- invariant：right = 当前组内所有气球右端的最小值 = 这一箭最晚能射的位置。

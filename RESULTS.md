
## ACT 20k run (Mac, batch 8, 51 min)
- l1_loss: 0.59 (start) -> 0.36 (5k) -> 0.28 (10k) -> 0.25 (15k) -> 0.22 (20k)
- Eval, 50 episodes each:
  | Steps | Success | Avg best overlap |
  |---|---|---|
  | 5k  | 2% | 0.27 |
  | 10k | 0% | 0.29 |
  | 15k | 2% | 0.34 |
  | 20k | 2% | 0.37 |
- Finding: best overlap rises steadily with training; success stays flat at 0-2% (noise).
  Success is a blind metric when the policy is far from the 95% bar.
- Suspect: ACT executes 100 actions open-loop. Test re-planning in Ship 2.

# Topic queue

The factory builds topics top to bottom by priority (1 = soon, 2 = normal, 3 = later). Add, reorder or delete rows freely; the `curriculum-planner` only appends, and refills the queue when fewer than `queue_min` topics are waiting. A topic leaves the queue's "waiting" count once it has a state file in `factory/state/`.

| priority | subject | topic | added_by |
|---|---|---|---|
| 1 | paediatrics | Tetralogy of Fallot | user: first research run |
| 1 | paediatrics | Transposition of the great arteries | seed: contrasts with TOF |
| 1 | paediatrics | Ventricular septal defect | seed: acyanotic CHD foundation |
| 2 | paediatrics | Patent ductus arteriosus | seed |
| 2 | paediatrics | Atrial septal defect | seed |
| 2 | paediatrics | Coarctation of the aorta | seed |

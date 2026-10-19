# Topic queue

The factory builds topics top to bottom by priority (1 = soon, 2 = normal, 3 = later). Add, reorder or delete rows freely; the `curriculum-planner` only appends, and refills the queue when fewer than `queue_min` topics are waiting. A topic leaves the queue's "waiting" count once it has a state file in `factory/state/`.

| priority | subject | topic | added_by |
|---|---|---|---|
| 1 | paediatrics | Tetralogy of Fallot | user: first research run |
| 1 | surgery | Acute appendicitis | user: 10 surgery modules |
| 1 | surgery | Inguinal hernia | user: 10 surgery modules |
| 1 | surgery | Acute intestinal obstruction | user: 10 surgery modules |
| 1 | surgery | Gallstones and acute cholecystitis | user: 10 surgery modules |
| 1 | surgery | Perforated peptic ulcer | user: 10 surgery modules |
| 1 | surgery | Carcinoma breast | user: 10 surgery modules |
| 1 | surgery | Thyroid nodule and differentiated thyroid cancer | user: 10 surgery modules |
| 1 | surgery | Burns: assessment and fluid resuscitation | user: 10 surgery modules |
| 1 | surgery | Trauma primary survey (ATLS) | user: 10 surgery modules |
| 1 | surgery | Varicose veins | user: 10 surgery modules |
| 2 | paediatrics | Transposition of the great arteries | seed: contrasts with TOF |
| 2 | paediatrics | Ventricular septal defect | seed: acyanotic CHD foundation |
| 2 | paediatrics | Patent ductus arteriosus | seed |
| 2 | paediatrics | Atrial septal defect | seed |
| 2 | paediatrics | Coarctation of the aorta | seed |

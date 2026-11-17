# Privacy Engineering Checklist: tick-box version

Copy this into a pull request or review ticket. Tick an item only after you ran its test. The full text, tests, sources and the list of what was not verified are in the [README](README.md). Sections 1 to 4 are blockers for launch. Sections 5 and 6 are hardening.


## 1. Data minimization and defaults

- [ ] **1.1** Every collected field maps to a documented purpose.
- [ ] **1.2** Defaults collect only what each purpose needs.
- [ ] **1.3** Personal data is not made accessible to an indefinite number of people by default.
- [ ] **1.4** Test and training environments contain no production personal data, or use a documented minimised subset.
- [ ] **1.5** Processing purposes are documented and enforced in the system.

## 2. Retention and deletion

- [ ] **2.1** Every data category has a written retention period and an owner.
- [ ] **2.2** An automated deletion job enforces each period.
- [ ] **2.3** The deletion job is tested and the evidence is kept.
- [ ] **2.4** User sessions expire after a configured idle time.

## 3. Data subject rights

- [ ] **3.1** A request workflow records the receipt date and computes a calendar-month due date.
- [ ] **3.2** An extension notice template exists and can be sent within the first month.
- [ ] **3.3** Deletion requests reach every system that holds the data, including processors.
- [ ] **3.4** (US, California) Global Privacy Control signals are honoured as an opt-out request.

## 4. Risk assessment, records and processors

- [ ] **4.1** A DPIA is completed **before** launch for processing that meets an Art. 35(3) trigger, and it contains the four Art. 35(7) elements.
- [ ] **4.2** A record of processing exists with the Art. 30(1) fields (purposes, categories, recipients, transfers, and retention and security descriptions where possible).
- [ ] **4.3** Each processor has a written contract covering Art. 28(3)(a) to (h).
- [ ] **4.4** Design review uses a privacy threat model such as LINDDUN (Linking, Identifying, Non-repudiation, Detecting, Data Disclosure, Unawareness, Non-compliance).

## 5. Security of processing and breach handling

- [ ] **5.1** Personal data is encrypted in transit and at rest, or the reason it is not is documented.
- [ ] **5.2** Pseudonymised data is classified as personal data in the data inventory.
- [ ] **5.3** A breach register exists and the runbook starts a 72-hour clock at awareness.
- [ ] **5.4** The runbook covers notifying data subjects without undue delay for likely high risk.
- [ ] **5.5** Security controls are tested on a schedule.

## 6. Privacy-enhancing technologies (PETs)

- [ ] **6.1** For each PET you use or reject (for example differential privacy, secure multiparty computation, homomorphic encryption, federated learning), the decision is recorded with the reason.

Result: ____ of 23 items ticked. Reviewer: ________  Date: ________

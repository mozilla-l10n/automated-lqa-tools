You are helping maintain a localization QA backlog for {language} (`{locale}`).

An automated reviewer raises findings on {language} translations. Each entry
below is a finding that was later dismissed as wrong, with the reason. The
`kind` says where the reason comes from:

- `rejected, reviewer's comment`: a {language} reviewer rejected the fix in
  Pontoon and said why. This is the strongest evidence.
- `rejected, reason inferred`: a reviewer rejected the fix without a comment,
  and a model guessed why. The rejection is a fact; the reason is a guess.
- `model`: a model asked to fix the finding judged it wrong and declined. No
  person has looked at it.

Each dismissal retires one string, so the reviewer keeps raising the same
mistaken finding on new strings. Your task is to find the **general rules**
of {language}, or of this locale's house style, that several of these
dismissals share, worded as an instruction to the reviewer that would have
stopped those findings being raised. A person will read each proposal and
decide whether to add it to the locale's conventions.

Rules:

- Propose a rule only when at least {min_strings} different strings were
  dismissed for the same underlying reason, and cite all of them by `ref`.
  A rule several reasons merely resemble is not enough.
- At least one cited entry must be a rejection (`rejected, …`). Agreement
  among `model` entries alone is a model agreeing with itself.
- State no more than the evidence supports. Prefer the narrow rule the
  entries show over a broad one they would also fit. Do not state a rule of
  {language} that no entry states or clearly implies.
- Where the evidence shows the boundary, say what remains a defect, so the
  rule cannot be read as excusing real errors.
- Give two or three examples taken from the entries.
- A reason that only says one string was fine, or that one finding misread
  its source, is not a rule.
- Leave out anything the conventions below already say, and anything that
  contradicts them.

Most of the time the correct answer is an empty list. Return one only when the
recurrence is plain.

Conventions recorded for this locale:

{conventions}

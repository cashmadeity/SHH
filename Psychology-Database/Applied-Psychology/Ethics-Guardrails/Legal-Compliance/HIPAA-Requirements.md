# HIPAA Requirements for Mental Health Apps

**Source:** U.S. Department of Health & Human Services (HHS), HIPAA Privacy Rule & Security Rule  
**Jurisdiction:** USA only (other countries have GDPR, Privacy Act, etc.)  
**Status:** Active as of 2026; regularly updated  

---

## What is HIPAA?

**HIPAA = Health Insurance Portability and Accountability Act**

It's a federal law that protects health information privacy and security. If you handle mental health data, **HIPAA likely applies to you.**

### Key Rule: Does HIPAA Apply to My App?

**YES, if you:**
- Collect health information (including mental health)
- Interact with healthcare providers, insurance companies, or health plans
- Are a "Business Associate" of a covered entity
- Store/process "Protected Health Information" (PHI)

**Maybe, if you:**
- Collect mental health data without medical provider involvement
- Are truly a consumer wellness app (not marketing as treatment)

**NO, if you:**
- Are purely a journaling/wellness app with no health claims
- Don't collect identifying information
- Don't interface with healthcare providers

**⚠️ Rule of thumb: If your app could help someone with a mental health condition, assume HIPAA applies. Better safe than sued.**

---

## Core HIPAA Obligations

### 1. Privacy Rule

**What it means:** Users have the right to know, access, and control their health information.

#### Key User Rights

- **Right to access:** User can request copy of all their data (within 30 days, reasonable fee)
- **Right to amend:** User can request corrections
- **Right to accounting:** User can request log of who accessed their data
- **Right to restrict:** User can request limits on use (e.g., "Don't share with insurance")
- **Right to confidentiality:** User can request that you not share data
- **Right to delete:** User can request deletion (within reasonable timeframe)

#### What This Means for Your App

✅ **Must do:**
- [ ] Provide easy way for user to download ALL their data (export function)
- [ ] Respond to data access requests within 30 days
- [ ] Allow user to request amendments (track changes, not delete history)
- [ ] Maintain audit log of who accessed data and when
- [ ] Allow user to delete data (unless legal hold, e.g., court order)
- [ ] Provide clear privacy policy explaining data use
- [ ] Notify user of any data breach <60 days (HIPAA Breach Notification Rule)

❌ **Cannot do:**
- [ ] Sell user health data (even de-identified)
- [ ] Share data with third parties without written consent
- [ ] Use mental health data for marketing
- [ ] Refuse to delete data (outside legal holds)
- [ ] Delay access requests unreasonably
- [ ] Hide data practices in fine print

### 2. Security Rule

**What it means:** You must protect health data from theft, loss, and unauthorized access.

#### Safeguards Required

**Physical Safeguards:**
- [ ] Servers in secure facility (locked, access controls)
- [ ] Computers/phones not left unattended with user data
- [ ] No printing PHI unless necessary (and destroying securely)

**Technical Safeguards:**
- [ ] Encryption at rest (AES-256 minimum)
- [ ] Encryption in transit (TLS 1.2+ minimum)
- [ ] Access controls (username/password, multi-factor auth)
- [ ] Audit logs (who accessed what, when)
- [ ] Regular security testing (pen tests, vulnerability scans)
- [ ] Data integrity controls (detect tampering)
- [ ] Backup and disaster recovery procedures

**Administrative Safeguards:**
- [ ] Security training for all staff (annually minimum)
- [ ] Designated Security Officer
- [ ] Risk assessment (what could go wrong?)
- [ ] Incident response plan (what if breached?)
- [ ] Business Associate Agreements with vendors
- [ ] Access controls (users can only see their own data)
- [ ] Documented security policies

#### Real-World Checklist

- [ ] Data encrypted at rest (not plaintext in database)
- [ ] HTTPS/TLS on all web/app connections (not HTTP)
- [ ] Access logs maintained (queryable by user)
- [ ] Password requirements: 12+ chars, complexity, regular changes
- [ ] Multi-factor authentication for admin access
- [ ] Penetration testing annually
- [ ] Staff security training documented
- [ ] Incident response plan written and tested
- [ ] Vendors sign Business Associate Agreements
- [ ] Data deletion verified (not just marked deleted)

### 3. Breach Notification Rule

**What it means:** If user data is stolen/lost/exposed, you must tell them quickly.

#### Timeline

1. **Discover breach** → Investigate immediately
2. **Within 60 days** → Notify affected individuals (by email/phone)
3. **Within 60 days** → Notify HHS Secretary (federal notification)
4. **Delayed notice allowed if** police investigation in progress (but still must eventually notify)

#### What to Include in Breach Notice

- [ ] What personal information was involved (mental health data, contact info, etc.)
- [ ] What happened (hacked, lost laptop, employee theft, etc.)
- [ ] When it happened
- [ ] What you're doing to fix it
- [ ] What users should do (monitor credit, change passwords, etc.)
- [ ] Contact info for questions

#### Example: "What NOT to Say"
❌ "We experienced a database migration issue. No data lost. Investigation ongoing."

**Why?** Vague. Users don't know if THEIR data is affected.

#### Example: "What to Say"
✅ "On March 15, we discovered unauthorized access to our user database. Your mental health journal entries for January-March may have been accessed. We've secured the server, encrypted all data, and notified law enforcement. Here's what to do: (1) monitor for identity theft, (2) consider freezing credit, (3) contact us if you have concerns. We're investigating fully and will provide updates."

---

## Business Associate Agreements (BAAs)

### What is a BAA?

A contract saying: "You'll handle our users' health data, and you agree to HIPAA-level security."

### When You Need One

**You need a BAA with:**
- Cloud services (AWS, Google Cloud, Azure)
- Email providers (if storing health data)
- Analytics tools (if processing health data)
- Backup services
- Any vendor accessing health data

**Example BAA checklist:**
- [ ] Vendor must encrypt data
- [ ] Vendor must have incident response plan
- [ ] Vendor must notify you of breaches
- [ ] Vendor must delete data on request
- [ ] Vendor must allow audits
- [ ] Vendor must restrict subcontractors

### BAA Template Sources

- HHS provides sample BAA language
- BAA Language: https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html

---

## Common Violations & How to Avoid Them

### Violation 1: Unencrypted Data

**What:** User mental health data stored in plain text in database.

**Risk:** Hacker steals database → accesses ALL user data

**Fix:**
```
❌ BAD:  database has columns:
   user_id | mood_journal | encrypted: false

✅ GOOD: database has columns:
   user_id | mood_journal_encrypted | encryption_key_id
   (encryption keys stored separately, rotated regularly)
```

---

### Violation 2: No Access Controls

**What:** Any employee can see any user's data.

**Risk:** Disgruntled employee steals data; attacker compromises employee account

**Fix:**
```
❌ BAD:  SELECT * FROM user_data; (anyone can run this)

✅ GOOD: Only users can see their own data (app enforces query):
   SELECT * FROM user_data WHERE user_id = <current_user_id>;
   
   Admin access is logged, restricted, and audited.
```

---

### Violation 3: Data Sold to Third Parties

**What:** App says "privacy policy" but sells anonymized mental health data to researchers/companies.

**Risk:** Violates user privacy, even if "de-identified"

**Fix:**
- Get explicit written consent: "You allow us to share your data for research with Company X"
- Only de-identify data that won't re-identify users (hard problem)
- Offer users ability to opt-out
- Use Business Associate Agreements

---

### Violation 4: No Breach Notification

**What:** App discovers hack March 1, tells users May 15 (105 days later).

**Risk:** Federal fine up to $1.5M per violation

**Fix:**
- Incident response plan: Discover → Investigate (24h) → Notify (within 60 days)
- Automated monitoring for breaches
- Pre-written breach notification templates
- Legal counsel on speed-dial

---

### Violation 5: Data Retention Without Justification

**What:** App keeps 10 years of user depression logs "just in case."

**Risk:** Violates user right to deletion; increases breach risk (more data = bigger target)

**Fix:**
- Retention policy: "Delete after 1 year inactivity" or "Delete after user closes account"
- Automatic deletion jobs (not manual)
- Archive old data encrypted and offline (not live database)

---

## HIPAA Compliance Checklist

### Before Launch

- [ ] **Privacy Policy**
  - Written in plain language (user can understand)
  - Disclose all data collection/uses
  - Explain user rights (access, delete, etc.)
  - State breach notification process

- [ ] **Encryption**
  - Data encrypted at rest (AES-256)
  - Data encrypted in transit (TLS 1.2+)
  - Encryption key management documented
  - No hard-coded secrets in code

- [ ] **Access Controls**
  - Users can only access their own data
  - Admin accounts restricted (not all employees have access)
  - Multi-factor authentication for admins
  - Access logs maintained

- [ ] **Vendors**
  - All vendors who touch health data have signed BAAs
  - Vendors assessed for security
  - Subcontractor security verified

- [ ] **Incident Response**
  - Plan written (what if breached?)
  - Roles assigned (who investigates? who notifies? who repairs?)
  - Tested (simulate breach, run drill)
  - Templates pre-written (breach notice, user notification)

- [ ] **Training**
  - All staff trained on HIPAA basics
  - Security training documented
  - Annual refresher scheduled

### Ongoing

- [ ] **Security Testing**
  - Penetration testing (annually minimum)
  - Vulnerability scanning (quarterly minimum)
  - Patch management (monthly minimum)
  - Log monitoring for suspicious activity (real-time)

- [ ] **Audits**
  - User data access audited
  - Encryption verified
  - Backup integrity tested
  - Third-party compliance verified

- [ ] **User Rights**
  - User can request data copy (respond <30 days)
  - User can request deletion (respond <30 days)
  - User can request access log (respond <30 days)
  - User can opt out of research/marketing (easily)

---

## Non-HIPAA Compliance (International & Consumer Apps)

### GDPR (Europe)

If you have EU users, GDPR likely applies (stricter than HIPAA):

- Explicit consent before data collection
- Right to deletion ("right to be forgotten")
- Data Protection Impact Assessment (DPIA) for high-risk processing
- Data Protection Officer (DPO)
- Breach notification <72h (vs HIPAA 60 days)
- Substantial fines ($10M+ possible)

**Key difference:** GDPR applies to *any* processing of personal data, not just health.

### CCPA (California)

If you have California users:

- Disclose data collection
- Right to access, delete, opt-out of sale
- No discrimination for exercising rights
- Fines $7,500 per violation

### HIPAA + GDPR + CCPA

**If you're international, expect to follow strongest rule for all:**

| Feature | HIPAA | GDPR | CCPA |
|---------|-------|------|------|
| Consent | Written consent | Explicit, informed, separate | Opt-out for sale |
| Encryption | Required | Required | Recommended |
| Breach notification | 60 days | 72 hours | Varies by state |
| Right to delete | Yes | Yes ("right to be forgotten") | Yes |
| Right to access | Yes | Yes | Yes |
| Data subject to rules | Health data | All personal data | Personal data |

**Best practice:** Follow GDPR + HIPAA + CCPA. They largely overlap.

---

## References

- **HIPAA Privacy Rule:** https://www.hhs.gov/hipaa/for-professionals/privacy/index.html
- **HIPAA Security Rule:** https://www.hhs.gov/hipaa/for-professionals/security/index.html
- **Breach Notification Rule:** https://www.hhs.gov/hipaa/for-professionals/breach-notification-rule/index.html
- **Sample Business Associate Agreement:** https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html
- **HHS HIPAA Enforcement:** https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/index.html
- **GDPR:** https://gdpr-info.eu/
- **CCPA:** https://oag.ca.gov/privacy/ccpa

---

## When to Consult a Lawyer

**DO consult a lawyer if:**
- You're unsure whether HIPAA applies to your app
- You're collecting health data and want to verify compliance
- You've suffered a data breach
- You want to publish research using user data
- You're expanding internationally
- You're considering a venture funding round (investors will ask about compliance)

**Cost:** Usually worth it (attorney review ~$5K) vs. fines (up to $1.5M+ per violation).

---

**Last reviewed:** 2026-03-20  
**Confidence level:** High (primary source: HHS)  
**Legal disclaimer:** This is guidance, not legal advice. Consult a healthcare attorney for your specific situation.

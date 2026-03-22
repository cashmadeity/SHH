# Data Security & Confidentiality in Assessment

**Source:** HIPAA Privacy & Security Rules; APA Standards 4.01 (Confidentiality); GDPR; best practices in clinical data security  
**Status:** Non-negotiable for ethical assessment  
**Scope:** Assessment data lifecycle security, access control, retention, breach response

---

## Why Assessment Data is Ultra-Sensitive

### The Stakes of a Breach

Assessment data = diagnosis, mental health history, vulnerabilities. If breached:

**For user:** Stigma, discrimination, blackmail, identity theft  
**For clinician:** Lawsuit, license revocation, criminal liability  
**For organization:** Massive fine (HIPAA: $100-50,000 per record), reputation destruction, shutdown

### Data Lifecycle (Where Breaches Happen)

```
Collection → Transmission → Storage → Access → Retention → Deletion

Each step is a vulnerability. Secure all 5.
```

---

## HIPAA Security Rule: Technical Safeguards

If you handle health information (diagnosis, assessment), you must follow HIPAA. Key requirements:

### 1. Encryption (At Rest & In Transit)

**At Rest** (data on your servers):
```
Requirement: Encrypted with AES-256 or equivalent
Verification: "aws s3 ls --sse-kms" or similar (use approved key manager)

NOT ACCEPTABLE:
❌ Unencrypted database
❌ Password-protected folders (not encryption)
❌ "We'll encrypt later"

ACCEPTABLE:
✅ Database encrypted with AES-256
✅ AWS KMS, Google Cloud KMS, or similar
✅ Encryption keys rotated quarterly
```

**In Transit** (data moving from app → server):
```
Requirement: TLS 1.2+ (no older protocols)
Verification: SSL/TLS certificate from trusted CA (not self-signed)
Test: https://www.sslshopper.com/ssl-checker.html (should get A+ rating)

NOT ACCEPTABLE:
❌ HTTP (unencrypted)
❌ TLS 1.0/1.1 (outdated)
❌ Self-signed certificates (vulnerable to MITM)

ACCEPTABLE:
✅ HTTPS with TLS 1.2+
✅ Certificate from Let's Encrypt or commercial CA
✅ HSTS header enabled (forces HTTPS)
```

### 2. Access Control

**Authentication** (who you are):
```
Requirement: Multi-factor authentication (MFA) for all staff accessing assessment data
Methods:
✅ Username + password + TOTP (Google Authenticator)
✅ Username + password + SMS (less ideal, acceptable)
✅ Biometric (fingerprint/face, if secure)

NOT ACCEPTABLE:
❌ Password only
❌ Shared passwords
❌ No MFA
```

**Authorization** (what you can access):
```
Requirement: Role-based access control (RBAC)
- Clinician A: Can only see own clients' results
- Admin: Can access user database but not assessment content
- Data analyst: Can see de-identified aggregates, not individual results

Rules:
✅ Principle of least privilege (minimum access needed)
✅ Clinician can't see another clinician's clients
✅ Admin can't see raw assessment data
✅ Staff access logged & auditable

NOT ACCEPTABLE:
❌ Everyone has admin access
❌ All staff can see all users
❌ No audit logs
❌ "It's fine, we trust our staff" (not a control)
```

**Session Management**:
```
Requirement: Sessions timeout after inactivity
- Typical: 15 minutes of no activity → automatic logout
- High-security: 5 minutes
- If accessing crisis/suicide data: 5 minutes mandatory

Implementation:
✅ Automatic logout with warning
✅ Session token with short expiry
✅ No "remember me" for sensitive data
✅ Clear session on logout
```

### 3. Audit Logging

**What to log:**
```
[ ] Who accessed what data
[ ] When (timestamp)
[ ] What they did (view/edit/delete)
[ ] From where (IP address)
[ ] Why (if applicable)

Example log entry:
"2026-03-21 14:23:45 | User: Dr_Smith | Action: Viewed PHQ-9 results | 
Patient: ID_12345 | IP: 192.168.1.100 | Purpose: Clinical review"

Retention:
- Keep logs for minimum 3-6 years (HIPAA requirement)
- Can't delete logs (potential cover-up)
- Regular audit of logs (monthly review for suspicious activity)
```

**Red flags in logs:**
```
[ ] User accessing patients they don't treat
[ ] Mass download of assessments (bulk theft?)
[ ] Access at unusual hours
[ ] Failed login attempts (brute force?)
[ ] Deletion of assessments (potential destruction of evidence)
```

### 4. Transmission Security

**Data in motion safeguards:**
```
HIPAA requires:
- Encryption during transmission
- Secure transmission mechanisms (not email, Slack, text)
- Integrity verification (data not modified in transit)

ACCEPTABLE:
✅ Secure portal (HTTPS encrypted)
✅ Encrypted email (PGP/S/MIME)
✅ Secure file transfer (SFTP, not FTP)

NOT ACCEPTABLE:
❌ Email (unencrypted)
❌ Text message
❌ Cloud storage link (Dropbox, Google Drive without encryption)
❌ Sending to wrong person (common breach type)
```

---

## Assessment Data Retention & Deletion

### How Long to Keep Assessment Data?

```
RETENTION POLICIES

Minimum legal holds:
- HIPAA: Keep records for minimum 6 years after last contact
- Some states: 7 years
- Minors: Until age 18 + some period (varies by state)
- Legal/forensic: Until case resolved, often longer

Practical retention:
- Active client: Keep indefinitely (or life of treatment + 7 years)
- Inactive client: 7 years after last contact, then delete
- Research (de-identified): Can keep longer if truly de-identified

Policies:
✅ Written retention schedule (documented, board-approved)
✅ Automatic deletion after retention period (not manual)
✅ Exception process (legal hold overrides deletion)
✅ Staff training on retention rules
```

### Secure Deletion

**Not OK:** Pressing "delete" button (data still on disk, recoverable)

**OK:** Cryptographic erasure or destruction
```
Methods:
1. Cryptographic erasure: Destroy encryption key (data unrecoverable)
   - Fast, effective, preferred
   
2. Degaussing: Use magnet to destroy hard drive (old data, not cloud)
   - Destructive, verify with third party
   
3. Physical destruction: Shred hard drive/destruction certificate
   - Expensive, use certified vendor
   
4. Overwriting: Write random data multiple times (NIST standard)
   - Time-consuming, less reliable than erasure
```

### User Right to Delete

**GDPR & CCPA: Right to be forgotten**

User can request deletion. Process:
```
1. User submits deletion request (in writing or portal)
2. You have 30 days to comply
3. You delete all personal data (encrypted so unrecoverable)
4. Exceptions:
   - Legal hold (court order, investigation)
   - Mandatory retention (medical records laws)
   - De-identified data (can keep if truly anonymized)
5. Confirm deletion to user

Don't:
❌ Ignore deletion requests
❌ Charge fees
❌ Delete selectively (keep some, delete others)
❌ Delay indefinitely
```

---

## De-Identification vs. Anonymization

### De-Identification (OK for HIPAA, but not always private)

**What:** Remove direct identifiers
- Remove name, address, phone, email
- Replace with ID number
- Keep clinical details

**Problem:** Re-identification risk
- Other clinical details might identify person anyway
- Vulnerable to linking attacks (combine with other datasets)

**When OK:** Approved by privacy officer, limited re-identification risk

### Anonymization (True Privacy)

**What:** Remove all identifiers AND any data that could identify

**Process:**
1. Remove all direct identifiers (name, contact, demographics)
2. Remove indirect identifiers (employer, rare conditions)
3. Aggregate data (only report on 50+ people, never individuals)

**Result:** Truly non-reidentifiable

**When to use:** For research sharing, public reporting

### Example

```
ORIGINAL ASSESSMENT DATA:
Name: John Smith
DOB: 1985-03-15
Address: 123 Main St, Springfield, OH 45231
PHQ-9 Score: 18 (moderate depression)
PTSD symptoms: Flashbacks of combat in Iraq, April 2023

DE-IDENTIFIED:
ID: P00123
Age: 38
Region: Midwest
PHQ-9 Score: 18
PTSD: Combat-related, 2023

ANONYMIZED:
(No ID, no name, no unique combination)
Aggregated: 50-person cohort
Average age: 35-45
Region: Midwest United States
% with moderate depression: 32%
% with combat-related PTSD: 18%
```

---

## Breach Response Plan

**If you suspect a breach:**

```
BREACH RESPONSE TIMELINE

IMMEDIATE (Within 1 hour):
[ ] Isolate affected systems (disconnect from network)
[ ] Preserve evidence (don't delete, don't overwrite)
[ ] Notify your security/IT team
[ ] Assess scope (how many records? what data?)

URGENT (Within 24 hours):
[ ] Confirm breach (not just suspicious activity)
[ ] Determine what was accessed
[ ] Launch forensic investigation
[ ] Notify your legal/compliance team
[ ] Prepare breach notice

NOTIFICATION (Within 60 days, per HIPAA):
[ ] Notify each affected individual
[ ] Notify media (if 500+ affected)
[ ] Notify HHS (Department of Health & Human Services)
[ ] Documentation: What happened, what you did, what's next

REMEDIATION (Ongoing):
[ ] Fix security vulnerability
[ ] Notify users of fix
[ ] Monitor for fraud (if payment data exposed)
[ ] Report to regulators if requested
[ ] Lawsuit mitigation (get insurance involved)
```

### Sample Breach Notification

```
BREACH NOTIFICATION LETTER

Dear [User Name],

We're writing to inform you of a security incident affecting your account.

WHAT HAPPENED:
On [date], we discovered unauthorized access to [our database].

WHAT DATA WAS AFFECTED:
- Your assessment results (PHQ-9, GAD-7)
- Your email address
- NOT: Your payment information (separate secure system)

WHAT WE'RE DOING:
- We've secured the vulnerability
- We've notified law enforcement
- We're offering free credit monitoring for 2 years
- We've updated our security

WHAT YOU CAN DO:
- Change your password immediately
- Monitor your accounts for fraud
- Call [fraud line] if you notice suspicious activity
- Contact us with questions

We apologize for this incident. Your privacy is our priority.

[Your organization]
```

---

## Third-Party Vendor Risk

If you use outside vendors (cloud storage, payment processor, etc.):

### Vendor Due Diligence

```
BEFORE SIGNING A CONTRACT:

[ ] Does vendor handle PHI (Protected Health Information)?
[ ] If yes, do you have a Business Associate Agreement (BAA)?
[ ] Vendor certifications: SOC 2 Type II? ISO 27001? (industry standards)
[ ] Audit: When did they last complete security audit?
[ ] Encryption: Do they encrypt data at rest & in transit?
[ ] Subcontractors: Who do they share data with? Get BAAs from them too
[ ] Breach notification: What's their process?
[ ] Right to audit: Can you audit their security?

Questions to ask:
- "Are you HIPAA-compliant?" (they should know)
- "Can you provide your SOC 2 audit report?" (proof)
- "What happens if there's a breach?" (documented plan)
- "Can we audit you if we want?" (they should say yes)

Red flags:
❌ "We handle security internally" (won't share details)
❌ No certifications or audits
❌ "We'll be HIPAA-compliant eventually"
❌ Unwilling to sign BAA
```

### Business Associate Agreement (BAA)

**What:** Legal contract with vendors handling your PHI

**Must include:**
```
[ ] Vendor will safeguard PHI
[ ] Vendor will use PHI only for your purposes
[ ] Vendor will encrypt/secure data
[ ] Vendor will notify you of breaches
[ ] You can audit vendor
[ ] Vendor will delete data on request
[ ] Vendor won't share data with subcontractors without BAA
[ ] Liability clauses if vendor breaches
```

**If vendor won't sign BAA:** Don't use them.

---

## Staff Training

### Everyone on Team Needs to Know

```
PRIVACY & SECURITY TRAINING (Annual minimum)

Content:
- What is PHI? (Protected Health Information)
- HIPAA basics (what's required)
- Password management (strong passwords, no sharing)
- Phishing awareness (don't click suspicious links)
- Social engineering (don't share info over phone)
- Proper disposal (don't throw away notes with patient names)
- Breach reporting (what to do if you suspect breach)
- Client confidentiality (when NOT to discuss cases)

Quiz/certification:
- Staff must pass test (80%+ passing score)
- Annual retesting
- Documentation: Training records kept

Real examples from your organization:
- Case study: How breach could happen here
- Exercises: What would you do?
- Consequences: Legal, professional, personal
```

---

## Data Security Checklist: Pre-Launch

```
ENCRYPTION
[ ] Data encrypted at rest (AES-256 or equivalent)
[ ] Data encrypted in transit (TLS 1.2+)
[ ] Encryption keys stored securely (key manager)
[ ] Key rotation plan (quarterly)

ACCESS CONTROL
[ ] Multi-factor authentication (MFA) for all staff
[ ] Role-based access control (RBAC)
[ ] Clinician sees only own clients
[ ] Admin access limited & logged
[ ] Session timeout after inactivity
[ ] No shared logins

AUDIT LOGGING
[ ] All access logged (who, when, what, where)
[ ] Logs retained 3-6 years
[ ] Logs not modifiable by users
[ ] Regular log review (monthly)
[ ] Suspicious activity alert system

RETENTION & DELETION
[ ] Retention policy documented
[ ] Automatic deletion after retention period
[ ] De-identification process defined
[ ] User deletion request process
[ ] Secure deletion method (cryptographic erasure)

THIRD-PARTY VENDORS
[ ] Vendor audited for security
[ ] Business Associate Agreement signed
[ ] BAA includes breach notification
[ ] Right to audit documented

BREACH RESPONSE
[ ] Breach response plan written
[ ] Roles assigned (who does what?)
[ ] Notification template prepared
[ ] Insurance in place
[ ] Legal counsel on speed dial

STAFF TRAINING
[ ] Annual privacy/security training (documented)
[ ] Staff certification (passed quiz)
[ ] Incident reporting clear (who to tell?)
[ ] Background checks done (if required)

COMPLIANCE
[ ] HIPAA risk assessment completed
[ ] Gaps identified & plan to fix
[ ] Regular compliance audits (annual)
[ ] Documentation of all security measures
[ ] Insurance coverage (cyber liability, errors & omissions)
```

---

## References

- HHS HIPAA Privacy Rule (45 CFR §164.400-414)
- HHS HIPAA Security Rule (45 CFR §164.302-318)
- GDPR Article 32 (Security of Processing)
- CCPA Section 1798.150 (Data Breach Notification)
- NIST Cybersecurity Framework

---

**Last reviewed:** 2026-03-21  
**Confidence level:** High (HIPAA/GDPR based, legal requirement)  
**Cross-references:** 01-Ethical-Assessment-Principles.md; 04-Informed-Consent-in-Assessment.md; 07-Assessment-Ethics-Audit-Framework.md

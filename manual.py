"""Knowledge base and system prompt for the Legal Rights Helper (India)."""

MANUAL = """
LEGAL RIGHTS GUIDE – INDIA (SUMMARY FOR CITIZENS)

NOTE: This is general information, not legal advice. Laws change and state rules differ.

IMPORTANT HELPLINES
- Police emergency: 112
- Cyber fraud / financial cyber crime: 1930 (also cybercrime.gov.in)
- Women helpline: 181
- Child helpline: 1098
- National Consumer Helpline: 1915 (also consumerhelpline.gov.in)
- Free legal aid (NALSA): 15100

1. FILING AN FIR (POLICE COMPLAINT)
- For a cognizable offence (serious crimes such as theft, assault, cheating), police must register an FIR. Since 1 July 2024 this falls under the Bharatiya Nagarik Suraksha Sanhita (BNSS), which replaced the CrPC.
- You can give the complaint orally or in writing. If oral, police must write it down and read it back to you.
- You are entitled to a FREE copy of the FIR.
- Zero FIR: you can file at ANY police station regardless of where the crime happened. It is then transferred to the right station.
- E-FIR / online complaints are available in many states for certain offences.
- If the police refuse, you can send the complaint in writing to the Superintendent of Police (SP/SSP), or approach the Magistrate.
- Police should not demand money to register an FIR.

2. RIGHTS ON ARREST
- You must be told the grounds of your arrest.
- You must be produced before a Magistrate within 24 hours (excluding travel time).
- You have the right to consult a lawyer of your choice.
- You have the right to have a relative or friend informed about the arrest.
- You cannot be forced to confess. Torture and custodial violence are illegal.
- Women should generally not be arrested between sunset and sunrise, except in exceptional cases with a Magistrate's written permission. Women should be arrested by women police officers.
- If you cannot afford a lawyer, you can get a free legal aid lawyer.

3. CONSUMER COMPLAINTS (Consumer Protection Act, 2019)
- You can complain about defective goods, deficient services, unfair trade practices, overcharging (above MRP) and misleading ads.
- Step 1: Send a written complaint or legal notice to the seller/company and keep proof.
- Step 2: Call 1915 or use the National Consumer Helpline for help with resolution.
- Step 3: File a case at the Consumer Commission online through e-Daakhil (edaakhil.nic.in) or in person.
- Which Commission: District Commission (goods/services value up to Rs 50 lakh), State Commission (above Rs 50 lakh up to Rs 2 crore), National Commission (above Rs 2 crore).
- Filing fee is nil for claims up to Rs 5 lakh.
- Time limit: generally within 2 years from the date the cause of action arose.
- You do not need a lawyer to file.
- Keep bills, receipts, warranty cards, screenshots and emails as evidence.

4. RIGHT TO INFORMATION (RTI Act, 2005)
- Any Indian citizen can ask a government department (public authority) for information.
- Application fee is usually Rs 10 for central government bodies (state fees may differ). It can be filed online at rtionline.gov.in for central departments.
- The department must reply within 30 days. If the matter concerns a person's life or liberty, within 48 hours.
- If there is no reply or the answer is unsatisfactory, file a First Appeal with the First Appellate Authority within 30 days.
- If still unsatisfied, file a Second Appeal with the Information Commission within 90 days.
- You do not have to give a reason for asking for information.
- Persons below the poverty line (BPL) are exempt from the fee.
- Some information is exempt (national security, personal privacy, etc.).

5. TENANT AND RENT RIGHTS
- Rent rules differ by state, so always check your state's rent law and your written rent agreement.
- Always sign a written rent agreement. Agreements longer than 11 months generally need registration.
- A landlord cannot lawfully evict you by force, cut off water or electricity, or lock you out. Eviction needs a legal process through the Rent Authority or Court.
- Security deposit: ask for a receipt. Many states allow deposits of only a limited number of months' rent, and the deposit should be returned after deducting only genuine damages and dues.
- Ask for rent receipts for every payment.
- The landlord generally must give proper written notice before asking you to vacate and before increasing rent, as per the agreement and state law.
- The landlord should give notice before entering the rented property, except in emergencies.

6. FREE LEGAL AID
- Free legal services are available to women, children, SC/ST persons, persons with disabilities, industrial workmen, persons in custody, victims of trafficking and disasters, and persons whose annual income is below the limit set by the State Legal Services Authority.
- Contact: District Legal Services Authority (DLSA) in your district court complex, or call 15100.
- Services include a free lawyer, help drafting documents and Lok Adalat.

7. LOK ADALAT (FREE SETTLEMENT)
- Lok Adalats settle disputes by mutual agreement without court fee.
- The award is final and binding, with no appeal.
- Suitable for cheque bounce, bank recovery, traffic challans, family and property disputes.

8. CYBER FRAUD / ONLINE SCAM
- Call 1930 immediately (the first hours matter for freezing money) and report at cybercrime.gov.in.
- Inform your bank right away and ask them to block the account/card.
- Keep screenshots, transaction IDs and phone numbers of the fraudster.

9. WORKPLACE RIGHTS
- Salary must be paid on time. Unpaid salary can be complained about to the Labour Commissioner/Labour Department.
- Women have the right to a workplace free from sexual harassment. Every workplace with 10 or more employees must have an Internal Committee (POSH Act, 2013).
- Employees covered under law have rights to provident fund, ESI and maternity benefits.

HOW TO ESCALATE ANY PROBLEM
Write a clear complaint with dates and proof, send it to the concerned authority, keep a copy, and if no action follows, approach the higher authority, the DLSA, or the court.
"""

SYSTEM_PROMPT = """
You are a Legal Rights Helper for ordinary citizens in India.
Answer only from the given guide.
If the answer is not available, say: Information not available in the guide. Please contact a lawyer or your District Legal Services Authority (helpline 15100).
Give simple, clear, step-by-step answers a non-lawyer can follow.
Reply in the same language the user writes in (English, Hindi or Punjabi).
Mention the relevant helpline or authority when useful.
End every answer with: This is general information, not legal advice.
"""

HELPLINES = [
    ("Police emergency", "112"),
    ("Cyber fraud", "1930"),
    ("Women helpline", "181"),
    ("Child helpline", "1098"),
    ("Consumer helpline", "1915"),
    ("Free legal aid (NALSA)", "15100"),
]

SAMPLE_QUESTIONS = [
    "Police are refusing to file my FIR. What can I do?",
    "My landlord locked me out. Is that legal?",
    "How do I file an RTI application?",
    "I lost money in an online scam. What should I do first?",
]

from app.parser.resume_parser import extract_text

from app.extraction.contact_extractor import (
    extract_email,
    extract_phone,
    extract_linkedin,
)

from app.extraction.skills_extractor import extract_skills


RESUME_PATH = "data/resumes/Dola_Vamsi_AI_ML_Internship_Resume.pdf"


def main():

    print("\n" + "=" * 60)
    print("          AI RESUME SCREENING SYSTEM")
    print("=" * 60)

    print("\nReading resume...")

    try:

        # Extract text from resume
        resume_text = extract_text(RESUME_PATH)

        print("Resume successfully processed! ✅")

        # Extract contact information
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        linkedin = extract_linkedin(resume_text)

        # Extract technical skills
        skills = extract_skills(resume_text)

        print("\n" + "=" * 60)
        print("              CANDIDATE INFORMATION")
        print("=" * 60)

        print(f"\nEmail:    {email}")
        print(f"Phone:    {phone}")
        print(f"LinkedIn: {linkedin}")

        print("\nSkills:")

        if skills:
            for skill in skills:
                print(f"  • {skill}")
        else:
            print("  No skills detected.")

        print("\n" + "=" * 60)
        print("                 RESUME TEXT")
        print("=" * 60)

        print(resume_text)

        print("\n" + "=" * 60)
        print("                    COMPLETE")
        print("=" * 60)

    except FileNotFoundError:

        print("\n❌ Resume file not found.")
        print(f"Expected file: {RESUME_PATH}")

    except ValueError as error:

        print(f"\n❌ {error}")

    except Exception as error:

        print(f"\n❌ Something went wrong: {error}")


if __name__ == "__main__":
    main()
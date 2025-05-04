def hospital_expert_system():
    print("Welcome to the Hospital Expert System!")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    # Ask the user about their symptoms
    fever = input("Do you have a fever? ").strip().lower()
    cough = input("Do you have a cough? ").strip().lower()
    sore_throat = input("Do you have a sore throat? ").strip().lower()
    chest_pain = input("Do you have chest pain? ").strip().lower()
    headache = input("Do you have a headache? ").strip().lower()
    stomach_pain = input("Do you have stomach pain? ").strip().lower()

    # Determine suggestions based on input
    if chest_pain == "yes":
        print("\nSuggestion: You should consult a cardiologist or go to the emergency room immediately.")
    elif fever == "yes" and (cough == "yes" or sore_throat == "yes"):
        print("\nSuggestion: You might be having a respiratory infection. Visit a general physician or an ENT specialist.")
    elif stomach_pain == "yes":
        print("\nSuggestion: You may need to see a gastroenterologist.")
    elif headache == "yes":
        print("\nSuggestion: Consider visiting a neurologist or a general physician.")
    else:
        print("\nSuggestion: Your symptoms appear mild. Monitor them, and if they worsen, consult your doctor.")

    print("\nThank you for using the Hospital Expert System!")

# Run the expert system
hospital_expert_system()
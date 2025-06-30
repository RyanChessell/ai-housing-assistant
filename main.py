# main.py

from agents.planner import plan_task
from agents.researcher import research_task
from agents.form_filler import fill_form
from agents.communicator import communicate

def main():
    user_input = "Help me apply for public housing in NYC"

    print("👤 User:", user_input)

    plan = plan_task(user_input)
    print("\n🧠 Planner says:", plan)

    resources = research_task(plan)
    print("\n🔍 Researcher says:", resources)

    form = fill_form(resources)
    print("\n📝 Form-Filler says:", form)

    result = communicate(form)
    print("\n📤 Communicator says:", result)

    print("\n🔍 Researcher found these resources:")
    for item in resources['top_results']:
        print(f"- {item['title']} → {item['link']}")

if __name__ == "__main__":
    main()


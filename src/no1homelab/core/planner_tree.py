class PlannerTree:
    """The 'Architect'. Creates a multi-step plan to achieve a goal."""

    def create_plan(self, intent: dict) -> list:
        """Creates a plan based on the understood intent. Placeholder logic."""
        plan = []
        action = intent.get("action")
        template = intent.get("template")

        if action == "scaffold":
            print(f"  - Generating scaffold plan for template: '{template}'")
            if template == "flask_basic":
                plan.append("CREATE_DIR: my_flask_app")
                plan.append("CREATE_FILE: my_flask_app/app.py")
                plan.append("CREATE_FILE: my_flask_app/requirements.txt")
                plan.append("CREATE_DIR: my_flask_app/templates")
                plan.append("CREATE_FILE: my_flask_app/templates/index.html")
            else:
                plan.append("CREATE_DIR: new_project")
                plan.append("CREATE_FILE: new_project/README.md")
                plan.append("CREATE_DIR: new_project/src")
        else:
            plan.append("ACTION: Clarify user request as it is unknown.")
        
        return plan

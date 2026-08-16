import streamlit as st
from bank import Bank


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Banking System",
    page_icon="🏦",
    layout="wide"
)


# =========================================================
# BANK OBJECT
# =========================================================

bank = Bank()


# =========================================================
# SESSION STATE INITIALIZATION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "account_number" not in st.session_state:
    st.session_state.account_number = None


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def logout():
    """Logout the current user."""

    st.session_state.logged_in = False
    st.session_state.account_number = None

    st.rerun()


def get_current_user():
    """Get the latest user data from the database."""

    if not st.session_state.account_number:
        return None

    return bank._find_by_account(
        st.session_state.account_number
    )


# =========================================================
# LOGIN / CREATE ACCOUNT PAGE
# =========================================================

if not st.session_state.logged_in:

    st.title("🏦 My Banking System")

    st.write(
        "Manage your bank account easily and securely."
    )

    st.divider()

    login_tab, create_tab = st.tabs(
        ["🔐 Login", "➕ Create Account"]
    )

    # =====================================================
    # LOGIN
    # =====================================================

    with login_tab:

        st.subheader("Login")

        with st.form("login_form"):

            account_number = st.text_input(
                "Account Number",
                placeholder="Enter your account number"
            )

            pin = st.text_input(
                "PIN",
                type="password",
                max_chars=4,
                placeholder="Enter 4 digit PIN"
            )

            login_button = st.form_submit_button(
                "Login",
                type="primary",
                use_container_width=True
            )

        if login_button:

            account_number = account_number.strip()
            pin = pin.strip()

            # -----------------------------
            # Validation
            # -----------------------------

            if account_number == "":
                st.error("Please enter your account number.")

            elif pin == "":
                st.error("Please enter your PIN.")

            elif not pin.isdigit():
                st.error("PIN must contain only numbers.")

            elif len(pin) != 4:
                st.error("PIN must contain exactly 4 digits.")

            else:

                user = bank.authenticate(
                    account_number,
                    int(pin)
                )

                if user:

                    st.session_state.logged_in = True
                    st.session_state.account_number = (
                        account_number
                    )

                    st.success("Login successful!")

                    st.rerun()

                else:

                    st.error(
                        "Invalid account number or PIN."
                    )

    # =====================================================
    # CREATE ACCOUNT
    # =====================================================

    with create_tab:

        st.subheader("Create New Account")

        with st.form("create_account_form"):

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=120,
                value=18,
                step=1
            )

            email = st.text_input(
                "Email",
                placeholder="example@gmail.com"
            )

            pin = st.text_input(
                "Create 4 Digit PIN",
                type="password",
                max_chars=4,
                placeholder="Enter 4 digit PIN"
            )

            confirm_pin = st.text_input(
                "Confirm PIN",
                type="password",
                max_chars=4,
                placeholder="Re-enter PIN"
            )

            create_button = st.form_submit_button(
                "Create Account",
                type="primary",
                use_container_width=True
            )

        # -------------------------------------------------
        # CREATE ACCOUNT VALIDATION
        # -------------------------------------------------

        if create_button:

            name = name.strip()
            email = email.strip()
            pin = pin.strip()
            confirm_pin = confirm_pin.strip()

            # Check name
            if not name:

                st.error(
                    "Please enter your name."
                )

            # Check email
            elif not email:

                st.error(
                    "Please enter your email."
                )

            # Check PIN
            elif not pin:

                st.error(
                    "Please enter a PIN."
                )

            elif not pin.isdigit():

                st.error(
                    "PIN must contain only numbers."
                )

            elif len(pin) != 4:

                st.error(
                    "PIN must contain exactly 4 digits."
                )

            # Check confirmation
            elif not confirm_pin:

                st.error(
                    "Please confirm your PIN."
                )

            elif pin != confirm_pin:

                st.error(
                    "PINs do not match."
                )

            # Everything valid
            else:

                success, result = bank.create_account(
                    name=name,
                    age=int(age),
                    email=email,
                    pin=int(pin)
                )

                if success:

                    st.success(
                        "🎉 Account created successfully!"
                    )

                    st.info(
                        f"""
                        **Your Account Number**

                        `{result["account_number"]}`

                        Please save this account number.
                        """
                    )

                else:

                    st.error(result)


# =========================================================
# MAIN DASHBOARD
# =========================================================

else:

    # Always get fresh data from JSON
    user = get_current_user()

    # -----------------------------------------------------
    # ACCOUNT NO LONGER EXISTS
    # -----------------------------------------------------

    if user is None:

        st.error(
            "Your account could not be found."
        )

        logout()

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.title("🏦 Banking System")

        st.divider()

        st.write(
            f"**Welcome, {user['name']}**"
        )

        st.write(
            f"Account: `{user['account_number']}`"
        )

        st.divider()

        page = st.radio(
            "Select Operation",
            [
                "🏠 Dashboard",
                "💰 Deposit",
                "💸 Withdraw",
                "👤 Account Details",
                "✏️ Update Account",
                "🗑️ Delete Account"
            ]
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout()

    # =====================================================
    # DASHBOARD
    # =====================================================

    if page == "🏠 Dashboard":

        st.title(
            f"👋 Welcome, {user['name']}"
        )

        st.write(
            "Here's an overview of your account."
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "💰 Current Balance",
                f"₹{user['balance']:,.2f}"
            )

        with col2:

            st.metric(
                "👤 Account Holder",
                user["name"]
            )

        with col3:

            st.metric(
                "🆔 Account Number",
                user["account_number"]
            )

        st.divider()

        st.subheader("Account Information")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Name:** {user['name']}"
            )

            st.write(
                f"**Age:** {user['age']}"
            )

        with col2:

            st.write(
                f"**Email:** {user['email']}"
            )

            st.write(
                f"**Balance:** ₹{user['balance']:,.2f}"
            )

    # =====================================================
    # DEPOSIT
    # =====================================================

    elif page == "💰 Deposit":

        st.title("💰 Deposit Money")

        st.metric(
            "Current Balance",
            f"₹{user['balance']:,.2f}"
        )

        st.divider()

        with st.form("deposit_form"):

            amount = st.number_input(
                "Amount",
                min_value=1,
                max_value=10000,
                value=100,
                step=100
            )

            deposit_button = st.form_submit_button(
                "Deposit Money",
                type="primary"
            )

        if deposit_button:

            success, result = bank.deposit(
                account_number=user["account_number"],
                pin=user["pin"],
                amount=amount
            )

            if success:

                st.success(
                    f"₹{amount:,.2f} deposited successfully!"
                )

                st.rerun()

            else:

                st.error(result)

    # =====================================================
    # WITHDRAW
    # =====================================================

    elif page == "💸 Withdraw":

        st.title("💸 Withdraw Money")

        st.metric(
            "Available Balance",
            f"₹{user['balance']:,.2f}"
        )

        st.divider()

        # Don't allow a withdrawal input greater
        # than the current balance.

        max_amount = int(user["balance"])

        if max_amount <= 0:

            st.warning(
                "You don't have sufficient balance."
            )

        else:

            with st.form("withdraw_form"):

                amount = st.number_input(
                    "Amount",
                    min_value=1,
                    max_value=max_amount,
                    value=min(100, max_amount),
                    step=100
                )

                withdraw_button = st.form_submit_button(
                    "Withdraw Money",
                    type="primary"
                )

            if withdraw_button:

                success, result = bank.withdraw(
                    account_number=user["account_number"],
                    pin=user["pin"],
                    amount=amount
                )

                if success:

                    st.success(
                        f"₹{amount:,.2f} withdrawn successfully!"
                    )

                    st.rerun()

                else:

                    st.error(result)

    # =====================================================
    # ACCOUNT DETAILS
    # =====================================================

    elif page == "👤 Account Details":

        st.title("👤 Account Details")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Personal Information")

            st.write(
                f"**Name:** {user['name']}"
            )

            st.write(
                f"**Age:** {user['age']}"
            )

            st.write(
                f"**Email:** {user['email']}"
            )

        with col2:

            st.subheader("Bank Information")

            st.write(
                f"**Account Number:** "
                f"`{user['account_number']}`"
            )

            st.write(
                f"**Balance:** "
                f"₹{user['balance']:,.2f}"
            )

    # =====================================================
    # UPDATE ACCOUNT
    # =====================================================

    elif page == "✏️ Update Account":

        st.title("✏️ Update Account")

        st.write(
            "Leave the PIN field empty if you don't "
            "want to change your PIN."
        )

        st.divider()

        with st.form("update_form"):

            new_name = st.text_input(
                "Name",
                value=user["name"]
            )

            new_email = st.text_input(
                "Email",
                value=user["email"]
            )

            new_pin = st.text_input(
                "New PIN",
                type="password",
                max_chars=4,
                placeholder="Leave empty to keep current PIN"
            )

            update_button = st.form_submit_button(
                "Update Account",
                type="primary"
            )

        if update_button:

            new_name = new_name.strip()
            new_email = new_email.strip()
            new_pin = new_pin.strip()

            # -----------------------------------------
            # Validation
            # -----------------------------------------

            if not new_name:

                st.error(
                    "Name cannot be empty."
                )

            elif not new_email:

                st.error(
                    "Email cannot be empty."
                )

            elif new_pin and (
                not new_pin.isdigit()
                or len(new_pin) != 4
            ):

                st.error(
                    "New PIN must contain exactly 4 digits."
                )

            else:

                pin_value = (
                    int(new_pin)
                    if new_pin
                    else None
                )

                success, message = bank.update_account(
                    account_number=user["account_number"],
                    pin=user["pin"],
                    name=new_name,
                    email=new_email,
                    new_pin=pin_value
                )

                if success:

                    st.success(message)

                    st.rerun()

                else:

                    st.error(message)

    # =====================================================
    # DELETE ACCOUNT
    # =====================================================

    elif page == "🗑️ Delete Account":

        st.title("🗑️ Delete Account")

        st.error(
            "⚠️ Warning: Account deletion is permanent."
        )

        st.write(
            "All account information will be removed "
            "from the database."
        )

        st.divider()

        confirm = st.checkbox(
            "I understand that my account will be permanently deleted."
        )

        if confirm:

            if st.button(
                "Delete My Account",
                type="primary"
            ):

                success, message = bank.delete_account(
                    account_number=user["account_number"],
                    pin=user["pin"]
                )

                if success:

                    st.success(message)

                    st.session_state.logged_in = False
                    st.session_state.account_number = None

                    st.rerun()

                else:

                    st.error(message)
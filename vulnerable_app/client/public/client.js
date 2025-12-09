if (typeof axios === 'undefined') {
    console.error("ERROR: axios is not loaded. Check internet connectivity or script load order.")
    alert("System Error: Network libraries failed to load.")
    throw new Error("Axios missing.")
}

axios.defaults.baseURL = 'http://localhost:5000'

let token = ''

// controller
async function userLogin() {
    try {
        // get user information from backend
        sending_data = {
            'user_id' : '1'
        }
        const response = await axios.post('login', sending_data);
        
        if (!response.data)
        {
            console.error(`Login failed: response is ${response}`);
        }

        token = response.data.token;
        let userData = response.data.user_pref;

        displayUser(userData);

        document.getElementById('login-view').classList.add('hidden');
        document.getElementById('user-pref-view').classList.remove('hidden');
    } catch (error) {
        console.error(`Login Failed: ${error.message}`)
    }
}

function displayUser(userData) {
    document.getElementById('name-display').innerText = userData.user_name;
    document.getElementById('role-display').innerText = userData.role;
}

function userLogout() {
    document.getElementById('login-view').classList.remove('hidden');
    document.getElementById('user-pref-view').classList.add('hidden');
    document.getElementById('name-display').innerText = '';
    document.getElementById('role-display').innerText = '';
}


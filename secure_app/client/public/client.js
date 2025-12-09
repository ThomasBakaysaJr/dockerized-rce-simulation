if (typeof axios === 'undefined') {
    console.error("ERROR: axios is not loaded. Check internet connectivity or script load order.")
    alert("System Error: Network libraries failed to load.")
    throw new Error("Axios missing.")
}

axios.defaults.baseURL = 'http://localhost:5000'

let token = ''

// controller
async function userLogin(loginId) {
    try {
        // get user information from backend
        sending_data = {
            'user_id' : loginId
        }
        const response = await axios.post('login', sending_data);
        
        if (!response.data)
        {
            console.error(`Login failed: response is ${response}`);
        }

        token = response.data.auth_token;
        let userData = response.data.user_data;

        displayUser(userData);

        document.getElementById('login-view').classList.add('hidden');
        document.getElementById('user-pref-view').classList.remove('hidden');
    } catch (error) {
        console.error(`Login Failed: ${error.message}`);
    }
}

async function accessAdmin() {
    try {
        console.log(`Token is ${token}`)
        config = {
            headers : {
                // 'Content-Type' : 'application/json',
                'Authorization' : `Bearer ${token}`
            }
        }

        console.log(config)

        const response = await axios.get('access_admin', config);

        if (!response.data)
        {
            console.error(`Elevate failed: response is ${response}`);
        }

        if (response.data.is_elevated) {
            displayAdmin();
        }

    } catch (error) {
        console.error(`Elevate Failed: ${error.message}`);
    }
}

function displayUser(userData) {
    document.getElementById('name-display').innerText = userData.user_name;
    document.getElementById('role-display').innerText = userData.role;
}

function hideUser() {
    document.getElementById('login-view').classList.remove('hidden');
    document.getElementById('user-pref-view').classList.add('hidden');
    document.getElementById('name-display').innerText = '';
    document.getElementById('role-display').innerText = '';
}


function displayAdmin() {
    document.getElementById('admin-enabled-view').classList.remove('hidden')
}

function hideAdmin() {
    document.getElementById('admin-enabled-view').classList.add('hidden')
}

function userLogout() {
    hideUser();
    hideAdmin();
}

if (typeof axios === 'undefined') {
    console.error("ERROR: axios is not loaded. Check internet connectivity or script load order.")
    alert("System Error: Network libraries failed to load.")
    throw new Error("Axios missing.")
}

const API_URL = 'http://localhost:5000'

let token = ''

// controller
async function userLogin() {
    try {
        // get user information from backend
        const response = await axios.post(API_URL/login);
        
        if (!response.data || !reponse.data.token)

        token = response.data.token;

        document.getElementById('login-view').classList.add('hidden');
        document.getElementById('user-pref-view').classList.remove('hidden');
    } catch (error) {
        console.log(`Login Failed: ${error.message}`)
    }
}

function userLogout() {
    document.getElementById('login-view').classList.remove('hidden');
    document.getElementById('user-pref-view').classList.add('hidden');
}


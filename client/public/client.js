console.log("Client.js loaded")

// view controller

async function userLogin() {
    try {
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
export function authHeader() {
    // return authorization header with jwt token
    let user = JSON.parse(localStorage.getItem('user'));

    if (user && user.token) {
        return { 'Authorization': 'Jwt ' + user.token };
    } else {
        return {};
    }
}
export function username() {
	let username = JSON.parse(localStorage.getItem('username'));
	if(username) {
		console.log(username)
		return username;
	} else {
		return 'temp_user';
	}
}
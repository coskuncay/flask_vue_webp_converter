import axios from "axios";

export function getApps() {
    axios.get('http://127.0.0.1:5000/api/apps').then(res => {
                return res
            })
}
        
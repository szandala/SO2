import axios from "axios";
import AuthHeader from "./AuthHeader";

const API_URL = "http://localhost:5000/";

const getPublicContent = () => {
  return axios.get(API_URL);
};

const getUserPage = () => {
  const header = AuthHeader()
  console.log({header})
  return axios.get(API_URL + "user", { headers: AuthHeader() });
};

const getModeratorBoard = () => {
  return axios.get(API_URL + "mod", { headers: AuthHeader() });
};

const getAdminBoard = () => {
  return axios.get(API_URL + "admin", { headers: AuthHeader() });
};

const UserService = {
  getPublicContent,
  getUserPage,
  getModeratorBoard,
  getAdminBoard,
};

export default UserService;

import React, { useState, useEffect } from "react";
import rajesh from "../rajesh.jpg"
import UserService from "../Services/UserService";

const Home = () => {
  const [content, setContent] = useState("");
  const [callRajesh, setCallRajesh] = useState(false);

  const image = <img src={rajesh}/>

  useEffect(() => {
    UserService.getPublicContent().then(
      (response) => {
        setContent(response.data.message);
        setCallRajesh(true);
      },
      (error) => {
        const _content =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
        setCallRajesh(false);
        setContent(_content);
      }
    );
  }, []);

  return (
    <div className="container">
      <header className="jumbotron">
        <h3>{content}</h3>
        {callRajesh && image}
      </header>
    </div>
  );
};

export default Home;

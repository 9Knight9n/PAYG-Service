import React, { useState, useEffect } from 'react';
import { Descriptions, Skeleton , Button  } from 'antd';
import {baseURL} from "../../components/config";


function Home (props) {
    const [loading, setLoading] = useState(false);
    const [loading1, setLoading1] = useState(false);
    const [loading2, setLoading2] = useState(false);
    const [loading3, setLoading3] = useState(false);
    const [totalCost, setTotalCost] = useState(null);
    const [monthlyCost, setMonthlyCost] = useState(null);
    const [id, setId] = useState(null);
    const [username, setUsername] = useState(null);

    useEffect(() => {
        fetchData()
    }, []);

    function fetchData() {
        setLoading(true)
        var myHeaders = new Headers();
        myHeaders.append("authorization", "token " + props.token);

        var requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        fetch(baseURL + "/api/auth/info/", requestOptions)
            .then(response => response.text())
            .then(response => {
                let temp = JSON.parse(response);
                setId(temp.id)
                setUsername(temp.username)
                setMonthlyCost(temp.monthly_cost)
                setTotalCost(temp.total_cost)
                setLoading(false)
            }).catch(error => console.log('error', error));
    }

    function callApi(api) {
        if(api===1)
            setLoading1(true)
        else if(api===2)
            setLoading2(true)
        else
            setLoading3(true)

        var myHeaders = new Headers();
        myHeaders.append("authorization", "token " + props.token);

        var requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        fetch(baseURL + "/api/payg/api"+api.toString()+"/", requestOptions)
            .then(response => response.text())
            .then(response => {
                let temp = JSON.parse(response);
                props.notif.success({
                    message: 'Called api' + api.toString() +' successfully.',
                    description: <pre>{JSON.stringify(temp, undefined, 2)}</pre>,
                    placement: 'top',
                });
                if(api===1)
                    setLoading1(false)
                else if(api===2)
                    setLoading2(false)
                else
                    setLoading3(false)
                fetchData()
            }).catch(error => console.log('error', error));
    }

    return (
        <div style={{display:'flex',flexDirection:'column',width:'600px'}}>
            <Descriptions column={3} title="User Info">
                <Descriptions.Item label="UserName" span={2}>{loading&&!username?<Skeleton.Button shape={'round'} active={true} block={true} size={'small'} />:username}</Descriptions.Item>
                <Descriptions.Item label="Total Cost" span={1}>{loading?<Skeleton.Button shape={'round'} active={true} block={true} size={'small'} />:totalCost}$</Descriptions.Item>
                <Descriptions.Item label="ID" span={2}>{loading&&!id?<Skeleton.Button shape={'round'} active={true} block={true} size={'small'} />:id}</Descriptions.Item>
                <Descriptions.Item label="Monthly Cost" span={1}>{loading?<Skeleton.Button shape={'round'} active={true} block={true} size={'small'} />:monthlyCost}$</Descriptions.Item>
                <Descriptions.Item span={3}><Button loading={loading1} onClick={()=>{callApi(1)}} style={{ width: "100%" }}>API 1</Button></Descriptions.Item>
                <Descriptions.Item span={3}><Button loading={loading2} onClick={()=>{callApi(2)}} style={{ width: "100%" }}>API 2</Button></Descriptions.Item>
                <Descriptions.Item span={3}><Button loading={loading3} onClick={()=>{callApi(3)}} style={{ width: "100%" }}>API 3</Button></Descriptions.Item>
            </Descriptions>
        </div>
    );
};
export default Home;
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_status : MonoBehaviour
{
    public TextMesh mTm;
    public string result;
    // Start is called before the first frame update
    void Start()
    {
        mTm = GetComponent<TextMesh>();
    }

    // Update is called once per frame
    void Update()
    {
        bool status1, status2, status3;
        status1 = Cb1.cb1_bool;
        status2 = Cb2.cb2_bool;
        status3 = Cb3.cb3_bool;
        uint working_status = Convert.ToUInt32(status1) + Convert.ToUInt32(status2) + Convert.ToUInt32(status3);

        if (working_status != 0) {
            result = working_status.ToString() + ":\t\tWorking";
        }
        else {
            result = "\tDone";
        }
        
        mTm.text = result;
    }
}



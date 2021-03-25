using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_default : MonoBehaviour
{
    public TextMesh mTm_group;

    // Start is called before the first frame update
    void Start()
    {
        mTm_group = GetComponent<TextMesh>();
        mTm_group.text = CylinderClass.cylinder_name.ToString();

        //Debug.Log("Text_default");
    }
    
    // Update is called once per frame
    void Update()
    {
        
    }
}

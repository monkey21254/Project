using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_Cube : MonoBehaviour
{
    public float mY = 0;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        mY = .005f;
        transform.Rotate(new Vector3(0, mY, 0));
    }
}

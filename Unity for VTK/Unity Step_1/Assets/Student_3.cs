using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Student_3 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // transform.Translate(53, 0, 4); // version 1
    }

    public float mX = 0, mY = 0, mZ = 0;
    // Update is called once per frame
    void Update()
    {
        if(mX < 47.5f){ // version 2
            mX += Time.deltaTime * 10.0f;
            transform.position = new Vector3(mX - 22.5f, 1, -10);
        } else if (mX >= 47.5f & mZ < 4.0f) {
            mZ += Time.deltaTime * 5.0f;
            transform.position = new Vector3(mX - 22.5f, 1, mZ - 10);
        }
    }
}

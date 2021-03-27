using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera_1 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        transform.Translate(0, 0, -10); // pair 1
    }

    //public float mX = 0;
    // Update is called once per frame
    void Update()
    {
        //if(mX - 25 <= 25) {
        //    mX += Time.deltaTime * 2f;
        //    transform.position = new Vector3(mX - 25, 5, 0);
        //} // pair 2
        //transform.Translate(0, 0, 0.1f); // pair 1
    }
}

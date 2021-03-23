using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Text_1 : MonoBehaviour
{
    public TextMesh mTm1;
    public float x, y, z;
    // Start is called before the first frame update
    void Start()
    {
        mTm1 = GetComponent<TextMesh>();
    }

    // Update is called once per frame
    void Update()
    {
        mTm1.text = Cb1.gText;
        transform.position = Cb1.cb_vec1;
        x = transform.position.x;
        y = transform.position.y;
        z = transform.position.z;
        transform.position = new Vector3(x, y - 1, z);
    }
}

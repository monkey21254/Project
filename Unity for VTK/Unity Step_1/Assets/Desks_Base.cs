using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Desks_Base : MonoBehaviour
{
    private GameObject deskObject;
    public GameObject desk_box;
    private GameObject[] desk_list = new GameObject[10];
    // Start is called before the first frame update
    void Start()
    {
        deskObject = (GameObject)Resources.Load("Prefabs/Desk");

        Debug.Log(desk_list.Length);

        for (int i = 0; i != desk_list.Length / 2; ++i)
        {
            for (int j = 0; j != desk_list.Length / 5; ++j)
            {
                desk_box = Instantiate(deskObject);
                desk_box.transform.Translate(i * 10, 0, j * -12);
                desk_box.transform.parent = gameObject.transform;
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

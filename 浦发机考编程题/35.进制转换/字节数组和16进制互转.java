
import java.util.*;
public class Main{

    private static final char[] Hexs = {
        '0', '1', '2', '3',
        '4', '5', '6', '7',
        '8', '9', 'A', 'B',
        'C', 'D', 'E', 'F'
    };

    // byte数组 转成 16进制大写字符串 
    public static String bytes2Hex(byte[] bytes){
        // 边界处理
        if (bytes == null || bytes.length == 0){
            return null;
        }

        StringBuilder hex = new StringBuilder();
        for (byte b : bytes){
            hex.append(Hexs[b>>4] & 0x0f);
            hex.append(Hexs[b & 0x0f]);
        }
        return hex.toString();
    }

    // 16进制字符串 转为 对应的byte数组
    public static byte[] hex2Bytes(String hex){
        if (hex == null || hex.length() == 0){
            return null;
        }

        char[] hChars = hex.toCharArray();
        byte[] bytes = new byte[hChars.length / 2];

        for(int i=0; i<bytes.length; i++){
            bytes[i] = (byte)Integer.parseInt("" + hChars[i * 2] + hChars[i * 2 + 1], 16);
        }

        return bytes;
    }

    //test
    public static void main(String[] args){
        String data = "Hello World";

        // byte[] to Hexs
        String hex = bytes2Hex(data.getBytes());
        System.out.println(hex); //48656c6c6f20576f726c64

        // Hexs to byte[]
        byte[] bytes = hex2Bytes(hex);
        System.out.println(new String(bytes)); // Hello World

    }

}
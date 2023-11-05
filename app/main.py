from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import barcode
from barcode.writer import ImageWriter
import qrcode
from io import BytesIO

app = FastAPI()

@app.get("/BarcodeCode128/{text}")
def generate_barcode(text: str):
    try:
        # Generate barcode
        barcode_code128 = barcode.get('code128', text, writer=ImageWriter())

        # Save barcode to a BytesIO object
        barcode_buffer = BytesIO()
        barcode_code128.write(barcode_buffer)
        
        # Seek to the start of the BytesIO buffer
        barcode_buffer.seek(0)
        
        # Stream the response back
        return StreamingResponse(barcode_buffer, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/QrCode/{text}")
def generate_qrcode(text: str):
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save it to a BytesIO object
        qr_buffer = BytesIO()
        img.save(qr_buffer, format="PNG")

        # Seek to the start of the BytesIO buffer
        qr_buffer.seek(0)
        
        # Stream the response back
        return StreamingResponse(qr_buffer, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

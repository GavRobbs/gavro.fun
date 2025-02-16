import ReactLogo from "../assets/react.svg"
import '../index.css'

export default function Entry(props){

    const image = "logo" in props ? props.logo : ReactLogo;

    return (
        <div className="entry-box" alt={props.title} onClick={() => {
            window.location.href = '/' + props.link;
        }}>
            {props.mobile_friendly && <span className="mobile-friendly">📱</span>}
            <img src={image} />
        </div>
    )
}
import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TwoRateThreeColorParameterFieldProps } from './two-rate-three-color-parameters';

export function TwoRateThreeColorBucketFSizeField(props: TwoRateThreeColorParameterFieldProps): ReactElement {
  const { twoRateThreeColorParameters, setTwoRateThreeColorParameters } = props;

  const twoRateThreeColorBucketFSize = useMemo(() => {
    return twoRateThreeColorParameters.bucketF_size || '';
  }, [twoRateThreeColorParameters]);

  const setTwoRateThreeColorBucketFSize = useSetNfvTeFunctionParameter('bucketF_size', setTwoRateThreeColorParameters);
  const onTwoRateThreeColorBucketFSizeChangeHandler = useChangeHandler(setTwoRateThreeColorBucketFSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket C"
      name="bucket-f-size"
      value={twoRateThreeColorBucketFSize}
      onChange={onTwoRateThreeColorBucketFSizeChangeHandler}
    />
  );
}
